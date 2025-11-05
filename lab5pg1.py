import calendar

# Get input from user
year = int(input("Enter a year: "))

# Check if it is a leap year
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
