# using default parameters.
def exponent(num, power = 2):
    return num ** power

print(exponent(2,3))
print(exponent(5))
print(exponent(7))

print("===========================================================================")
def add(a=10, b=20):
    return a + b

print(add())
print(add(5,7))

def show_information(first_name='Steven', is_instructor=False):
    if first_name == 'Steven' and is_instructor:
        return "Welcome back instructor Steven"
    elif first_name == 'Steven':
        return "I really thought you were an instructor..."
    return f"Hello {first_name}"

print("===========================================================================")
print(show_information())
print(show_information(is_instructor=True))
print(show_information('Molly'))

print("===========================================================================")
def addition(a,b):
    return a + b

def math(a,b, fn=addition):
    return fn(a,b)

def subtract(a,b):
    return a-b

print(math(2,2)) # 4
print(math(2,2, subtract)) # 0