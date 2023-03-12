# A Python program with variables, while loop, list, and user input.

name_list = []  # Initialize an empty list for storing names.

while True:
    name = input("Enter your name: ")
    new_user = input("Are you a new user? (y/n) ")

    if new_user == "y":
        name_list.append(name)  # Add the new user to the list of names.
        print(f"Hello, {name}!")
        break
    elif new_user == "n":
        if name_list:  # Check if the list of names is not empty.
            print(f"Welcome back, {name_list[0]}!")
            break
        else:
            print("Sorry, we could not find your name. Please try again.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")