# Day to Weekend Checker
# Ask user to enter a day of the week.
# If it's Saturday or Sunday → "It's weekend!"
# If it's Monday to Friday → "Working day!"
# Else → "Invalid day"

day = str(input("enter your day = ")).lower()

weekday = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend =  ["saturday", "sunday"]
if day in weekend:
    print("it's weekend")
elif day in weekday:
    print("working day")
else:
    print("invalid day")
