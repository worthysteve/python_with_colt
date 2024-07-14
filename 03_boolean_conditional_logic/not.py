age = 21
# 2-8, $2 ticket
# 65 or > $5 ticket
# $10 for everyone

if not((age >= 2 and age <= 8) or (age >= 65)):
    print("You pay $10, you are not a child or senior")
else:
    print("you are a child or senior")