# Print square root of negative or positive number using if and operators
a =int(input("Enter a number and I'll get its square root: "))
if a >= 0:
    print(f"The square root of {a} is {a**0.5}")
if a <= 0:
    print("I can't calculate the square root of a negative number!")
print('thanks for the input!')   

# We can also use Logical Operators like OR and AND.

c=str(input("Enter Country's name: "))
if c == 'Pakistan' or c == 'pakistan':
    print("You are from Pakistan")
else:
    print("You are not from Pakistan")
