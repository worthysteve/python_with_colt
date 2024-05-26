# Extremes Exercise - Using Min and Max
# Write a function called extremes  which accepts an iterable. It should return a tuple containing the minimum and maximum elements.  For example:

# extremes([1,2,3,4,5])  # (1, 5)

# extremes((99,25,30,-7))  # (-7, 99)

# extremes("alcatraz")  #( 'a', 'z')

# REMEMBER, RETURN A TUPLE!!!

# Define extremes below:
def extremes(lst):
    return tuple([min(l for l in lst), max(l for l in lst)])

print(extremes([1,2,3,4,5]))
print(extremes((99,25,30,-7)))
print(extremes("alcatraz"))

# Extremes Solution
# This solution is pretty straightforward:

# I call min(nums) and max(nums)
# I wrap the values I get back in a new tuple and return it!


def extremes(nums):
    return(min(nums), max(nums))

print(extremes([1,2,3,4,5]))
print(extremes((99,25,30,-7)))
print(extremes("alcatraz"))