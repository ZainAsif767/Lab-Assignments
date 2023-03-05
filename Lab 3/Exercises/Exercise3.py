# Practicing import Modules

# instead of importing a full library we can import the module that best suites
# and we can also change the function name like

import random
import glob
import time
from math import sqrt as squareroot
print("SquareRoot:", squareroot(49))


# time module returns the current time in seconds
print("Time Module:", time.time())
# however , ctime converts it to the human readable form
current_time = time.time()
print("Current Time Module:", time.ctime(current_time))

# time.sleep(n) waits for at least n seconds and then returns:
# print(time.sleep(4))

# Glob module
# returns all files of all types of extension
print("Print File ending on any extension:", glob.glob("*"))
# returns all files with txt extension
print("Print File ending on .txt:", glob.glob("*.txt"))

# Random module
# random.random() generates a real-valued random number in the interval (0,1)
print("Random no between 0 and 1:", random.random())

# random.randint(a, b) generates a real valued random number between a & b inclusive
print("Random no between specified integers:", random.randint(1, 100))

# random.shuffle(list) permutes the list into a random ordering in place.
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print("Random Shuffle:", lst)

# random.sample(list,k) randomly selects k elements from list (k cannot exceed len(list)) and
# returns a new list containing those elements:

lst1 = [6, 7, 8, 9, 10]
random.sample(lst1, 2)
print("Random sample:", lst1)
