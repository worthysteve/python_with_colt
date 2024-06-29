
# partition
# Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ). 

# The function should iterate over each element in the list and invoke the callback function at each iteration. 

# If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# When it's finished, partition should return both lists inside of one larger list, like so:

# [truthy_list, falsy_list] 

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(lst, callback):
    return [[i for i in lst if callback(i)], [i for i in lst if not callback(i)]]



def isEven(num):
    return num % 2 == 0

print(partition([1,2,3,4], isEven) )# [[2,4],[1,3]]

# "Traditional" Version
# Here's my solution that doesn't use a list comprehension:

# I have two lists, to hold the true and false values

# I loop through the list, calling fn  with each value in the list

# If the result is True, I append the value to the trues  list

# Otherwise, I append the value to the falses  list

# At the end I return a list that contains both the trues  and falses  lists

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

print(partition([1,2,3,4], isEven) )# [[2,4],[1,3]]


# Another Solution (updated)
# This solution was originally submitted by a student named Jonathan.  Thanks, Jonathan!

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l[:] if callback(i)], l]

print(partition([1,2,3,4], isEven) )# [[2,4],[1,3]]

