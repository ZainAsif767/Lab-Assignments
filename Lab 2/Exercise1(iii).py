# Exercise 1 (iii)
pass_word = "abc$123"
a = str(input("Enter Password : "))
i = 1
while (a != pass_word):
    print("I don't know you")
    a = str(input("Enter password again : "))
    i += 1
    if i >= 5:
        print("Try again after 5 minutes")
        break
print("Welcome!")
