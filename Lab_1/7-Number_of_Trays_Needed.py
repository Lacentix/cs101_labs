# This is a program that calculates the number of trays needed to hold X glasses.
# Given that a tray can hold 5 glasses.

from math import ceil

glasses = int(input("Enter the number of glasses: "))

trays_req = ceil(glasses / 5)

# TODO: Improve these if statements.
if glasses == 1:
    glass: str = "glass"
else:
    glass: str = "glasses"

if trays_req == 1:
    tray: str = "tray is"
else:
    tray: str = "trays are"

# TODO: Improve this print statement.
print(trays_req, tray, "needed", "to hold", glasses, glass)
