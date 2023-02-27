# Python program to square and cube every number in a
# given list of integers using Lambda.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The original list:", lst)
squared_list = list(map(lambda x: x**2, lst))
print("Squared list: ", squared_list)
cube_list = list(map(lambda x: x ** 3, lst))
print("Cube list: ", cube_list)
