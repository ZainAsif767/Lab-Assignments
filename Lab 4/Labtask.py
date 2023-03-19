from abc import abstractmethod

class Environment:

    @abstractmethod
    def __init__(self, n):
        self.n = n
    def executeStep(self,n=1): 
        raise NotImplementedError('action must be defined!')
    def executeAll(self): 
        raise NotImplementedError('action must be defined!')
    def delay(self,n=100): 
        self.delay = n

class Room:
    def __init__(self,location,status="dirty"):
        self.location = location
        self.status = status

class TwoRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room('A','dirty') 
        self.r2 = Room('B','dirty') 
        self.agent = agent 
        self.currentRoom = self.r1 
        self.delay = 100
        self.step = 1 
        self.action = ""
    def executeStep(self,n=1): 
        for _ in range(0,n):
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
    def executeAll(self): 
        raise NotImplementedError('action must be defined!')
    def displayPerception(self): 
        print("Perception at step %d is [%s,%s]"%(self.step,self.currentRoom.status,self.currentRoom.location))
    def displayAction(self): 
        print("------- Action taken at step %d is [%s]" %(self.step,self.action))
    def delay(self,n=100):
        self.delay = n

class Agent:

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def sense(self,environment): 
        pass
 
    @abstractmethod 
    def act(self):
        pass

class VaccumAgent(Agent):
    def __init__(self):
        pass
    def sense(self,env):
        self.environment = env
    def act(self): 
        if self.environment.currentRoom.status == 'dirty': return 'clean'
        if self.environment.currentRoom.location == 'A': return 'right' 
        return 'left'    
    
vcagent = VaccumAgent()
env = TwoRoomVaccumCleanerEnvironment(vcagent) 
env.executeStep(50)