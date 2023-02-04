# (ii) Write a Python program to convert
# to and from celsius and Farenheit.
print("1 = Celsius", " | ", "2 = Farenheit")
choice = float(input("Enter your Choice: 1 or 2"))
if (choice == 1):
    celsius = float(input("Enter Temp in Celsius"))
    Farenheit = (celsius*9/5) + 32
    print(Farenheit)
elif (choice == 2):
    Farenheit = float(input("Enter Temp in Farenheit"))
    celsius = (Farenheit - 32) * 5 / 9
    print(celsius)
else:
    print("invalid input")
