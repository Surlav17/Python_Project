# Arithmetic Operations (5 Practice Questions)
# Basic Calculator
# Ask the user to enter two numbers and perform: addition, subtraction, multiplication, and division. Display results using f-strings.

x = float(input("Enter the value of x = "))
y = float(input("Enter the value of x = "))

add = x+y
sub = x-y
mul = x*y
div = x/y

print(f"value after add = {add}")
print(f"value after sub = {sub}")
print(f"value after mul = {mul}")
print(f"value after div = {div}")


# Area of a Circle
# Ask the user for the radius. Calculate the area using π × r² (use 3.14 as pi). Show the result.

radius = float(input("Enter the radius of your circle = "))
area = 3.14 * radius**2

# print(area)

# Average of Three Numbers
# Ask the user to input three numbers. Calculate and print the average.
#
a,b,c = map(float,input("Enter the numbers =").split())

avg = (a+b+c)/3
print(avg)

# Simple Interest Calculator
# Formula: SI = (P × R × T)/100
# Ask for Principal, Rate, and Time, and show the Simple Interest.

P,R,T = map(float, input("enter the values of P, R,T =").split())

SI = (P*R*T)/100
print(SI)



