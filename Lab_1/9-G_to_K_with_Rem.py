# This is a program that converts from grams to kilograms with the remainder in grams.
# 1KG = 1000G

from math import modf

grams = int(input("Enter weight in grams: "))

kg_to_g = grams // 1000
remainder = (grams / 1000) % 1

# TODO: Improve these if statements.
if kg_to_g == 1:
    kg: str = "kilogram"
else:
    kg: str = "kilograms"

if grams == 1:
    g: str = "gram is"
else:
    g: str = "grams are"

if remainder == 1:
    g_rem: str = "gram."
else:
    g_rem: str = "grams."

# TODO: Improve this print statement.
print(grams, g, kg_to_g, kg, "and", remainder, g_rem)
