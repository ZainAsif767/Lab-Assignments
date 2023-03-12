# Of course, operators can also be combined using parentheses:

a = int(input("Enter a number between 10-20 or 30-40: "))
if (a >= 10 and a <= 20) or (a >= 30 and a <= 40):
    print("The condition has been met.")
else:
    print("You did it wrong.")