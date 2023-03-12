# Write a Python script to concatenate
# following dictionaries to create a new one.

# Given Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

final_dictionary = {}
final_dictionary.update(dic1)
final_dictionary.update(dic2)
final_dictionary.update(dic3)

print(final_dictionary)
