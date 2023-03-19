from modules.VaccumAgent import VaccumAgent
# from modules.TwoRoomVacCleaner import TwoRoomVaccumCleanerEnvironment
from modules.ThreeRoomVacCleaner import ThreeRoomVaccumCleanerEnvironment
# from modules.nRoomVacCleaner import nRooomVaccumCleanerEnvironment


vcagent = VaccumAgent()
env = ThreeRoomVaccumCleanerEnvironment(vcagent)
env.executeStep(20)

# the code creates an instance of the VaccumAgent class and an instance
# of the TwoRoomVaccumCleanerEnvironment class, and executes 50 steps in
# the environment using the executeStep() method.
