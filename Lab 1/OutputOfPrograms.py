# x = 6
# if (type(x) is int):
#     print("true")
# else:
#     print("false")

#  (i) Use dir and help to learn about the
#  functions you can call on dictionaries
#  and implement it.
# dic1 = {'Apple': 20, 'Banana': 40, 'Mango': 75}
# dic2 = {'Kiwi': 110, 'Orange': 90}

# print(dic1.items())
# print(dic1.values())
# print(dic2.get('Orange'))
# print(dic2.keys())
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
# for item in list1:
#     if item in list2:
#         print("overlapping")
#     else:
#         print("not overlapping")
a = 60
b = 13
c = 0
c = a & b
print("Line 1", c)
c = a | b
print("line 2", c)
c = a ^ b
print("line 3", c)
c = ~a
print("line 4", c)
c = a << 2
print("Line 5", c)
c = a >> 2
print("Line 6", c)
