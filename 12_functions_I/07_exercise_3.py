# Yell Function Exercise
# Implement a function yell  which accepts a single string argument.  It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  For example:

# yell("go away")   # "GO AWAY!"

# yell("leave me alone")   # "LEAVE ME ALONE!"

# You do not need to call the function to pass the tests.

def yell(x):
    return f"{x.upper()}!"

print(yell("go away"))

# Using string concatenation:

def yell(word):
    return word.upper() + "!"

print(yell("Steven"))

# Using the string format() method:

def yell(word):
    return "{}!".format(word.upper())

print(yell("Code"))