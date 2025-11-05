import time
from datetime import datetime

# Get current date and time
current_time = datetime.now()

print("a) Current date and time:", current_time)
print("b) Current year:", current_time.year)
print("c) Month of the year:", current_time.month)

# Using time module for week details
week_number = time.strftime("%U")
weekday_name = time.strftime("%A")
day_of_year = time.strftime("%j")
day_of_month = current_time.day
day_of_week = current_time.strftime("%w")

print("d) Week number of the year:", week_number)
print("e) Weekday of the week:", weekday_name)
print("f) Day of year:", day_of_year)
print("g) Day of the month:", day_of_month)
print("h) Day of week:", day_of_week)
