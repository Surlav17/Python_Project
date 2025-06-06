# Input a sentence. Count how many vowels (a, e, i, o, u) are in it.

string= str(input("please enter an string: "))

vowel = ["a", "e", "i", "o", "u"]
count = 0

for i in string.replace(" ",'').lower():
    if i in vowel:
        count += 1
        print(i)
print(f"total number of vovel = {count}")



