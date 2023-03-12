# Fixed a Letter from a to e and then ask the user to guess that
# letter until correct letter entered.

value = 'c'
guess = input("Guess the letter from a to e: ")
while guess != value:
    print("incorrect")
    guess = input("Guess the letter again: ")
print("welcome user!")
