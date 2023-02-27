# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number
# of cities from the keyboard and store the data in a file in the order in which they’re entered.

city = str(input("Name of City: "))
population = str(input("Enter Population: "))
mayor = str(input("Name of Mayor: "))

with open("cities.txt", "a") as f:
    f.write(f"City - {city}  Population - {population} Mayor - {mayor}\n")
    f.close()
