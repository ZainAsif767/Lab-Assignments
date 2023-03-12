# A python program having variables, while loop
# list, user input.
while True:
    name = input("Enter Your name : ")
    name_list = []
    newuser = input('New user ? y or n')
    if newuser == "y":
        name_list.append(name)
        print("Hello", name_list[0])
        break
    elif newuser == "n":
        print("Hello Existing User")
        break
    else:
        print("Please try again")
