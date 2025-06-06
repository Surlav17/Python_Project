# Even or Odd Counter
# Ask the user to input 10 numbers. Count how many are even and how many are odd.

numbers = input("Enter 10 numbers separated by spaces: ").split()

even_count = 0
odd_count = 0

for num_str in numbers:
    num = int(num_str)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")







