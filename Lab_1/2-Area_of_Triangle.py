# This is a program that calculates the area of a triangle.
# Went with floats just in case the users inputs a decimal.

base = float(input("Enter a base: "))
height = float(input("Enter height: "))
area: float = base * height * 0.5

print("The area of the triangle is", area)
