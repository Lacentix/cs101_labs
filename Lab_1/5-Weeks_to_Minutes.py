# This is a program that converts from weeks to minutes.
# A week has 7 days, and 7 days are 24 hours and an hour
# is 60 minutes.
# (7 * 24) * 60 = 10080

week_num = int(input("Enter the number of weeks: "))

week_to_min: int = week_num * 10800

if week_num == 1:
    week: str = "week is"
else:
    week: str = "weeks are"

print(week_num, week, week_to_min, "minutes.")
