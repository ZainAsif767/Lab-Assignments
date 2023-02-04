# Write a list comprehension which from a list,
# generates a lowercased version of each string
# that has length greater than five.

strings = ['PAKISTAN', 'ITALY', 'BANGLADESH', 'CHINA']
string_lowerCase = [s.lower() for s in strings if len(s) > 5]
print(string_lowerCase)
