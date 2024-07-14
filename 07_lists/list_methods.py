data = [1,2,3]

# Append
data.append('purple')
print(data)

# Extend - adds multiple elements to a list
nums = [1,2,3]

nums.extend([4,5])
print(nums)

# INSERT - inserts eleemts at any index we want to
nums = [1,2,3,4]

nums.insert(len(nums), "LAST")
print(nums)

# clear
items = ['socks', 'mug', 'tea pot', 'cat food']
print(items)
items.clear()

# pop
items = ['socks', 'mug', 'tea pot', 'cat food']
print(items.pop())
print(items.pop(1))

# remove
names = ['colt', 'blue', 'arya', 'lena', 'steve', 'selena', 'pable']
print(names.remove('blue'))

# index
numbers = [5,5,6,7,8,9,10]
print(numbers.index(5))
print(numbers.index(5, 1))

# print(names.index('colt', 1))

print(names.count('selena'))

another_list = names.reverse()
print(another_list)

# join
words = ['Coding', 'is', 'fun!']
joined = ' '.join(words)
print(words)
print(joined)

friends = " ".join(names)
print(f"I am friends with {friends}!")