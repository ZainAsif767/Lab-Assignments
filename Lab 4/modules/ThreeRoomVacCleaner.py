'''
from modules.Environment import Environment
from modules.Room import Room


class ThreeRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom == self.r1:
                    self.currentRoom = self.r2
                else:
                    self.currentRoom = self.r3
            elif res == 'left':
                if self.currentRoom == self.r2:
                    self.currentRoom = self.r3
                else:
                    self.currentRoom = self.r1

            self.displayAction()
            self.step += 1

            if self.r1.status == 'clean' and self.r2.status == 'clean' and self.r3.status == 'clean':
                print('All rooms are clean. Stopping the agent.')
                return

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n
'''
# Scoring for Agent
from modules.Environment import Environment
from modules.Room import Room


class ThreeRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score = 0

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                if self.currentRoom.status == 'dirty':
                    self.score += 25
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom == self.r1:
                    self.currentRoom = self.r2
                else:
                    self.currentRoom = self.r3
                self.score -= 1
            elif res == 'left':
                if self.currentRoom == self.r2:
                    self.currentRoom = self.r3
                else:
                    self.currentRoom = self.r1
                self.score -= 1

            if self.r1.status == 'dirty':
                self.score -= 10
            if self.r2.status == 'dirty':
                self.score -= 10
            if self.r3.status == 'dirty':
                self.score -= 10

            self.calculateScore()
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" %
              (self.step, self.action))

    def delay(self, n=100):
        self.delay = n

    def calculateScore(self):
        print("Score at step %d is %d" % (self.step, self.score))
