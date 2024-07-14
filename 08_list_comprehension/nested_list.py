nested = [[1,2,3], [4,5,6], [7,8,9]]
print(nested[0][1])
print(nested[1][-1])

for nest in nested:
    for val in nest:
        print(val)

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for location in coords:
    print(location)

for location in coords:
    for coord in location:
        print(coord)

[[print(val) for val in nest] for nest in nested]

board = [[num for num in range(1, 4) for val in range(1,4)]]
print(board)

game = [['x' if num % 2 != 0 else 'o' for num in range(1,4)] for val in range(1,4)]
print(game)

initial = [["*" for x in range(1,4)] for i in range(1,4)]
print(initial)