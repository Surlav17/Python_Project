# calculate the average height from a list of height.
# cannot use sum() and len(). need to use input(). need answer in whole number.

list = input("please enter the height:")

count = 0
for i in list:
    count += 1
print("length=", count)

average = sum(list)
print(average/5)
