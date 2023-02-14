# Exercise 1 (ii)
eff = float(input("Enter time(Hours) taken by worker to complete a task: "))
if eff >= 1 and eff <= 3:
    print("The Worker is higly efficient")
elif eff > 3 and eff <= 4:
    print("The Worker should improve speed!")
elif eff > 4 and eff <= 5:
    print("The Worker needs training")
else:
    eff > 5
    print("The Worker is fired")
