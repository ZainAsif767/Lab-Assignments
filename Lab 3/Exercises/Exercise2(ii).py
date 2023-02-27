# Python program to create a data file student.txt and append the message “Now we are
# AI students”s

file = open("student.txt", "x")
file = open("student.txt", "a")
file.write("Now we are AI student's.")
file.close()
