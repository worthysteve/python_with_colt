print(abs(-23))

# maths.fabs treats everything as float
import math

print(math.fabs(-4)) # e.0


# sum
print(sum([1,2,3]))
print(sum([1,2,3], 30))
print(sum([1,2,3], -6))
print(sum([1.5,2,3.7]))
print(sum({1,50,100}))

# print(sum(['hi', 'there'])) # error

# round
print(round(3.512345))
print(round(3.512345, 3))
print(round(3.512345, None))
print(round(9.9999999999999999999999999999, 15)) # 10.0