# age = int(input("Enter your age: "))
#
# if age >= 18:
#     nationality = input("Are you Indian? (yes/no): ")
#     if nationality == "yes":
#         print("You are eligible to vote.")
#     else:
#         print("You must be an Indian citizen to vote.")
# else:
#     print("You must be at least 18 years old to vote.")


Pizza = input("what pizza you are looking for:")
small = 100
med = 200
lar = 300
pep_small = 10
pep_med, pep_lar = 20, 20
ext = 30

if small:
    pep_small == input("do you want peporoni: (Y/N)" )
    if pep_small == "yes":
        ext == input("do you want extra cheese")
        if ext == "yes":
            print(f"your bill is{small + pep_small + ext}")

    else:
        print(f"your bill is{small}")