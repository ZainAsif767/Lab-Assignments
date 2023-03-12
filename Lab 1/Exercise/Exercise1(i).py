# Exercise Python input /output Basic operations
# (i)Write a Python program to swap 4 variables values
a = 2
b = 56
c = 78
d = 9
print("Before Swapping")
print("a =", a, "b =", b, "c =", c, "d =", d)
# Swapped a and d
tempVariable = a
a = d
d = tempVariable
# Swapping b and c
temp2 = b
b = c
c = temp2
print("After Swapping")
print("a = ", a, " d =", d)
print("b = ", b, "c = ", c)
