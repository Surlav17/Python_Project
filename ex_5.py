# Find Maximum from a List
# Take 5 numbers from the user and store them in a list. Find and print the maximum number.

# Assume the first element is the greatest.
# Loop through the list starting from the second element.
# Compare each element with the current greatest.
# Update the greatest if a larger number is found.
# Return or print the final greatest number after the loop.


number = input("please enter 5 numbers: ")
greatest = number[0]

for i in number[1:]:

    if i > greatest:
        greatest = i
print(f"The greatest number is: {greatest}")

