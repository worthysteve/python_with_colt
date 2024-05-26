
# multiply_even_numbers
# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(numbers):
    product = 1
    for number in numbers:
        if number % 2 == 0:
            product = product * number
    return product

print(multiply_even_numbers([2,3,4,5,6]))