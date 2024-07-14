# Another List Comp Exercise
# For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)

# USE A LIST COMPREHENSION.

answer = [divisible for divisible in range(100) if divisible % 12 == 0]
print(answer)

answer2 =  [multiples for multiples in range(1, 101) if multiples % 12 == 0]
print(answer2)