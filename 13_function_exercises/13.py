
# intersection
# Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.

# intersection([1,2,3], [2,3,4])    #[2,3]
# intersection(['a','b','z'], ['x','y','z']) .  # ['z']


# flesh out intersection pleaseeeee
def intersection(lst1, lst2):
    return [i for i in lst1 if i in lst2]

print(intersection([1,2,3], [2,3,4]) )
print(intersection(['a','b','z'], ['x','y','z']) )

# Manual Looping Solution
# Here's one potential solution:

# Define an empty list that will eventually store the in common values
# Loop through one list (l1)
# For each value, check if that value is in the other list (l2)
# If it is, append the value to the in_common list
# Return in_common  after the loop ends

def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

print(intersection([1,2,3], [2,3,4]) )
print(intersection(['a','b','z'], ['x','y','z']) )

# List Comprehension Solution
# The first solution is perfectly valid.  It's a more "traditional" way of solving the problem.  A more Python-ic solution involves using a list comprehension to do the same thing on a single line. Both work just as well.  It's a matter of personal preference, so don't get too caught up in it!

def intersection(l1, l2):
    return [val for val in l1 if val in l2]

print(intersection([1,2,3], [2,3,4]) )
print(intersection(['a','b','z'], ['x','y','z']) )

# Sets Solution
# This solution(submitted by Sebastian on the discussion boards) is the most efficient of the three.  It converts the lists to sets, which removes duplicate values, and then finds the intersection of them using &.  If you need review, watch the sets section again (it's super short).

def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

print(intersection([1,2,3], [2,3,4]) )
print(intersection(['a','b','z'], ['x','y','z']) )