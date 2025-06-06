# Sum of Natural Numbers
# Ask the user to enter a number n, and calculate the sum of numbers from 1 to n.

n = int(input("Enter a positive number: "))
if n > 0:
    total = n * (n + 1) // 2
    print(f"The sum of natural numbers from 1 to {n} is {total}")
else:
    print("Please enter a positive number.")
