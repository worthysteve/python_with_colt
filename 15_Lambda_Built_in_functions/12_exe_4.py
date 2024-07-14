
# Any/All Exercise
# Implement a function is_all_strings  that accepts a single iterable and returns True if it contains ONLY strings.  Otherwise, it should return false.  

# is_all_strings(['a', 'b', 'c'])  #True

# is_all_strings([2,'a', 'b', 'c'])  #False

# is_all_strings(('hello', 'goodbye'))  #True

# Implement your is_all_strings function below:
def is_all_strings(itr):
    return all([type(x) == str for x in itr])

print(is_all_strings(['a', 'b', 'c'])) #true
print(is_all_strings([2,'a', 'b', 'c']))#false
print(is_all_strings(('hello', 'goodbye')))#true


print('===================================')
# Using a Generator Expression

# I start by defining is_all_strings, which accepts a parameter called lst
# I call the built-in function all, passing in a generator expression that checks if the type of each item in the list is a str.  

def is_all_strings(lst):
    return all(type(l) == str for l in lst)

print(is_all_strings(['a', 'b', 'c'])) #true
print(is_all_strings([2,'a', 'b', 'c']))#false
print(is_all_strings(('hello', 'goodbye')))#true