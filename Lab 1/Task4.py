# Write a Python program to count the number
# of strings where the string length is 2 or
# more and the first and last character are
# same from a given list of strings.

def stringCounter(list):
    count = 0
    for s in list:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count


sample_list = ['zain', 'pakistan', 'asia', 'europe']
results = stringCounter(sample_list)
print("Answer", results)
