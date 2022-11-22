# This is a program that distributes apples N apples on a group of 7 with the remainder.

apple_num = int(input("Enter the amount of apples: "))
groups = apple_num // 7
remainder = apple_num % 7

# TODO: Improve these if statements.
if apple_num == 1:
    apple: str = "apple"
else:
    apple: str = "apples"

if groups == 1:
    group_num: str = "group"
else:
    group_num: str = "groups"

if remainder == 1:
    apple_rem: str = "apple"
else:
    apple_rem: str = "apples"

# TODO: Improve this print statement.
print(apple_num, apple, "will feed", groups, group_num, "with", remainder, apple_rem, "left.")
