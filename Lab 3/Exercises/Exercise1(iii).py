# Python program to extract year, month, date and time using Lambda
import datetime
currentDateTime = datetime.date(2023, 2, 27)
print(currentDateTime)
def year(x): return x.year
def month(x): return x.month
def day(x): return x.day


print('Year - ', year(currentDateTime))
print('Month - ', month(currentDateTime))
print('Day - ', day(currentDateTime))
