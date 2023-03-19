# For the Two Room Vacuum Cleaner Environment

from modules.Environment import Environment
from modules.Room import Room


class TwoRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 100
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
                self.currentRoom = self.r2
            else:
                self.currentRoom = self.r1
            self.displayAction()
            self.step += 1

            '''
            @this code makes the program stop by checking the clean condition
            if self.r1.status == 'clean' and self.r2.status == 'clean':
                print('All rooms are clean. Stopping the agent.')
                return
            '''

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

# The TwoRoomVaccumCleanerEnvironment class is a subclass of Environment that models
# a two-room environment. It has two room objects r1 and r2 which are instances of
# the Room class. It also has an agent object agent and a current room object currentRoom.
# The agent is an instance of the VaccumAgent class, which is a subclass of Agent and
# implements its sense() and act() methods. The executeStep() method defines the actions
# to be taken by the agent in the environment. If the current room is dirty, the agent
# cleans it; otherwise, it moves to the next room based on its location. Finally, the
# displayPerception() and displayAction() methods display the current perception
# and action of the agent.
