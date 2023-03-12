# Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between
a = int(input()) # the variable is initialized with a value of 0
if a == 1: # if the value is 1, we change its value to 0
    a = 0
if a == 0: # if the value is 0, we change its value to 1
    a = 1
if a>2 or a<0:
    print("You have entered number between")
print(a)
    