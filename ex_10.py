# 2. Prime Number Checker (Range)
# Ask the user to input a number n. Print all prime numbers from 1 to n using a loop.

# If the number is less than or equal to 1 → not prime.
# If the number is 2 or 3 → prime.
# For numbers > 3:
# Try dividing the number by all integers from 2 up to √n.
# If any of them divides the number completely (i.e., remainder is 0), then it is not prime.
# If none divide it, then it is prime.

num = int(input("Enter a number: "))

for i in range(1, num):
    i += 1
    if i>=1 and i%2 == 0 and i**0.5:
        print(f"This is a prime number {i}")




