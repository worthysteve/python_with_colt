colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[2:])

colors2 = colors[:]
print(colors2)

print(colors[-2])

print(colors[: 5])
print(colors[2:4])

print(colors[1::2]) # step 2
print(colors[::2]) # step 2
print(colors[:1: -2]) # step 

string = 'This is fun!'

print(string[::-1])

numbers = [1,2,3,4,5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers)