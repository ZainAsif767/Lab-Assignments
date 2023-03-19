from modules.Environment import Environment
from modules.Room import Room


class nRooomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, rooms):
        self.rooms = [Room(location, 'dirty') for location in rooms]
        self.agent = agent
        self.currentRoomIndex = 0
        self.currentRoom = self.rooms[self.currentRoomIndex]
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for i in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoomIndex += 1
                if self.currentRoomIndex == len(self.rooms):
                    self.currentRoomIndex = 0
                self.currentRoom = self.rooms[self.currentRoomIndex]
            elif res == 'left':
                self.currentRoomIndex -= 1
                if self.currentRoomIndex < 0:
                    self.currentRoomIndex = len(self.rooms) - 1
                self.currentRoom = self.rooms[self.currentRoomIndex]

            self.displayAction()
            self.step += 1
            for i in self.rooms:
                if i.status == 'clean':
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                print("All Rooms are clean,stopping agent")
                return

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s, %s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n
