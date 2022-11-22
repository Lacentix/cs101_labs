# This is a program that calculates the distance between two points.

from math import sqrt
from math import pow

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance: float = sqrt((pow(x2 - x1, 2)) + pow(y2 - y1, 2))
print("The distance is: ", distance)
