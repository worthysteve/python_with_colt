def square(num): return num * num

print(square(9))

square2 = lambda num: num * num
print(square2(7))

add = lambda a, b: a + b

print(add(3, 10))

print(square.__name__)
print(square2.__name__) # no name
print(add.__name__) # no name