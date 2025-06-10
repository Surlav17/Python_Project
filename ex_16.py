# Assignment and Comparison Operators (5 Practice Questions)
# Compare Two Numbers
# Ask the user to enter two numbers. Use comparison operators (==, !=, <, >, <=, >=) to compare them and print appropriate messages.

a,b = map(float, input("Enter two numbers separated by space: ").split())
if a == b:
    print("both numbers are equal")
elif a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
elif a >= b:
    print(f"{a} is greater than or equal to {b}")
elif a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print("Invalid comparison")

# Check if User is Eligible to Vote
# Ask for the user's age. If age is greater than or equal to 18, print "Eligible to vote", else print "Not eligible".

age = int(input("Please enter your age: "))
if age >=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
