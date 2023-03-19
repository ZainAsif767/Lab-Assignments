# Vaccum Agent Class

from modules.agent import Agent
class VaccumAgent(Agent):
    def __init__(self):
        pass
    def sense(self,env):
        self.environment = env
    def act(self): 
        if self.environment.currentRoom.status == 'dirty': return 'clean'
        if self.environment.currentRoom.location == 'A': return 'right' 
        return 'left'
    
# The VaccumAgent class is a subclass of Agent that implements the sense() 
# and act() methods. The sense() method takes the environment object as input
# and the act() method defines the actions of the agent. In this code, the agent
# cleans the room if it is dirty and moves to the next room based on its location.    