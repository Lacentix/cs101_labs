# This is a program that converts from days to hours with the remainder.
# A day has 24 hours

day_num = float(input("Enter the number of days: "))

day_to_hour: float = day_num * 24
remainder = day_to_hour % 24

# TODO: Improve these if statements.
if day_num > 1:
    day: str = "day is"
else:
    day: str = "days are"

if day_to_hour <= 1:
    hour: str = "hour"
else:
    hour: str = "hours"

if remainder <= 1:
    rem_hour: str = "hour"
else:
    rem_hour: str = "hours"

# TODO: Improve this print statement.
print(day_num, day, day_to_hour, hour, "with", remainder, rem_hour, "left")
