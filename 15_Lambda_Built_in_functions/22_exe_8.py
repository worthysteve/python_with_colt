
# sum_floats
# Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    return sum(a for a in args if type(a) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1,2,3,4,5))