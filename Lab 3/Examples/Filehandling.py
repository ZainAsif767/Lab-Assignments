# opening the demo file and appending content
f = open("demofile.txt", "a")
f.write("Zain Asif")
f.close()

# Opening and read file after apending
f = open("demofile.txt", "r")
print(f.read())

# open the demo file and overwite the content
f = open("demofile.txt", "w")
f.write("Erasing Content")
f.close()

# # Create a file called "myfile.txt"
f = open("myfile.txt", "x")
