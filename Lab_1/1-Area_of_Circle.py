# This is a program that calculates the area of a circle.
# Went with floats just in case the users inputs a decimal.

from math import pi
from math import pow

radius = float(input("Enter a Radius: "))
area: float = pow(radius, 2) * pi

print("The area the circle is", area)
