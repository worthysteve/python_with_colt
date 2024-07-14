
# Greatest Magnitude Exercise
# Write a function max_magnitude  that accepts a single list full of numbers. It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).

# max_magnitude([300, 20, -900])   #900

# max_magnitude([10, 11, 12])   #12

# max_magnitude([-5, -1, -89])   #89

# Hint: use max and abs!

def max_magnitude (numbs):
     return max(abs(num) for num in numbs)

print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]) )
print(max_magnitude([-5, -1, -89]))