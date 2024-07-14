numbers = [1,2,3,4]

for number in numbers:
    print(number)

print("============== THIS IS ANOTHER EXAMPLE ===========================")
colors = ['purple', 'teal', 'magenta']

for color in colors:
    print(color)

print("============== THIS IS ANOTHER EXAMPLE ===========================")
numbers = [4,6,2,9,7,10]
for num in numbers:
    print(num * num)

print("============== USING A WHILE LOOP ===========================")
numbers = [1,2,3,4]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

print("============== ANOTHER WHILE LOOP EXAMPLE ===========================")
colors = ['purple', 'teal', 'magenta', 'crimson', 'emerald']

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1