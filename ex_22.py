# Time-Based Greeting System
# Ask user to enter time (24-hour format).
# 0–11: Good Morning
# 12–17: Good Afternoon
# 18–20: Good Evening
# 21–23: Good Night
# Else print invalid time.

time = float(input("please enter the time in 24 hour format = "))

if time >0 and time <=11:
    print("Good Morning")
elif 12 < time <=17:
    print("Good Afternoon")
elif 18 < time <=20:
    print("good evening")
elif 21 < time <=23:
    print("Good Night")
else:
    print("invalid time")
