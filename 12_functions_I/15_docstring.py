# using document string (docstring)
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello"

print(say_hello.__doc__)

print.__doc__
# print(random.randint.__doc__)

def exponent(num, power = 2):
    """exponent(num, power) raises num to specified power. Power defaults to 2"""
    return num ** power

print(exponent(2,3))
print(exponent(5))
print(exponent(7))

print(exponent.__doc__)