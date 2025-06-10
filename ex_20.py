#  Check Triangle Type
# Ask the user to input three sides of a triangle.
# Then:
# Check if the sides can form a triangle.
# A triangle is valid only if the sum of any two sides is greater than the third.
# If valid, print:
# "Equilateral triangle" if all sides are equal.
# "Isosceles triangle" if any two sides are equal.
# "Scalene triangle" if all sides are different.
# If not valid, print "Not a triangle".

a,b,c = map(float,(input("enter three sides of a triangle = ")))

if a == b == c:
    print("This is an equilateral triangle")
elif a == b and c > a:
    print("this is isosceles triangle")
elif a!=b!=c:
    print("this is scalene triangle")
