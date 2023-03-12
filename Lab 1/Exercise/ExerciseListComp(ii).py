# Write a Python program to print a specified
# list after removing the 0th, 4th & 5th elements ?


list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
print("List before = ", list)
list = [elements for elements in list if elements not in (
    'Red', 'Pink', 'Yellow')]
print("List After = ", list)
