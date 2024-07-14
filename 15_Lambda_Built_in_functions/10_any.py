print(any([0,1,2,3])) # True, because any uses the OR conditional while all uses the AND conditional

nums = [2,60,26,18]
print(any([num % 2 == 0 for num in nums])) # true

nums = [2,60,26,18, 21]
print(any([num % 2 == 0 for num in nums])) # true

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
