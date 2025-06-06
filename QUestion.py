#area - 1/2*b*h


b = input("Enter value of b = ")
if b.replace('.', '',).isdigit():
    b = float(b)
    print(b)
else:
    print("Please enter a numeric value")
    exit()
h = input("Enter value of h = ")
if h.replace('.', '', 2).isdigit():
    h = float(h)
    print(h)
else:
    print("Please enter a numeric value")
    exit()

area = 1/2 * b * h
print(f"Area = {area}")

