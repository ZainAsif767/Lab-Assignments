#Take collection of number input from user. Print the total positive and negative number.

# counting positive and negative numbers
pcount = 0
ncount = 0
count = int(input("how many numbers you want? "))
i = 1 # initialization
while i <= count: # condition
    num = int(input("Enter a number: "))
    if num > 0:
        pcount += 1
    else:
        ncount += 1
    i += 1 # increment
print("Positive numbers: ", pcount)
print("Negative numbers: ", ncount)

        