# Vowel and Consonant Counter
# Ask the user to input a sentence. Count how many vowels and consonants are present.

line = input("Please enter a sentence: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in line:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Total vowels: {vowel_count}")
print(f"Total consonants: {consonant_count}")

