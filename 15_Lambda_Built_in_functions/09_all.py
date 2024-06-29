print(all([1,2,3,4,5])) # True

print(all([char for char in 'eio' if char in 'aeiou'])) # true


people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
print(all([name[0] == 'C' for name in people]))
print([name[0] == 'C' for name in people])
people.append('Steven')
print([name[0] == 'C' for name in people])

nums = [2,60,26,18]
print(all([num % 2 == 0 for num in nums])) # true

nums = [2,60,26,18, 21]
print(all([num % 2 == 0 for num in nums])) # false