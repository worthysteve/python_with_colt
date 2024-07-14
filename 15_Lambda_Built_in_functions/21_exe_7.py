
# sum_even_values
# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!

# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values
def sum_even_values(*args):
   return sum(num for num in args if num % 2 ==0)
   

print(sum_even_values(1,2,3,4,5,6)) # 12
print(sum_even_values(4,2,1,10)) # 16
print(sum_even_values(1)) # 0