# Exercise 1 ( i )
height = int(input("Enter Height: "))
width = int(input("Enter Width: "))
depth = int(input("Enter Depth: "))
volume = height * width * depth
if volume >= 1 and volume <= 10:
    print(volume, "cm^3")
    print("Extra small")
elif volume >= 11 and volume <= 25:
    print(volume, "cm^3")
    print("Small")
elif volume >= 26 and volume <= 75:
    print(volume, "cm^3")
    print("Medium")
elif volume >= 76 and volume <= 100:
    print(volume, "cm^3")
    print("Large")
elif volume >= 101 and volume <= 250:
    print(volume, "cm^3")
    print("Extra Large")
else:
    volume >= 251
    print(volume, "cm^3")
    print("Extra-Extra Large")
