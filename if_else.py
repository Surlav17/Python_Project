

E = float(input("enter the number:"))
M = float(input("enter the number:"))
S = float(input("enter the number:"))

score = (E+M+S) / 3

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
elif 0 <= score < 60:
    print("Grade F")
else:
    print("Invalid score")



