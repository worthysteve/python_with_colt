nums = [2,4,6,8,10]

doubles = map(lambda x: x * 2, nums)
for num in doubles:
    print(num)


print(list(doubles))

people = ['Darcy', 'Christiana', 'Dana', 'Anabel']
peeps = map(lambda name: name.upper(), people)
# for person in peeps:
#     print(person)
print(list(peeps))

l = [1,2,3,4]
doubles = list(map(lambda x: x*2, l))
print(doubles)

names  = [
    {'first': 'Steven', 'last': 'Daniel'},
    {'first': 'Umu-Hawa', 'last': 'Barrie'},
    {'first': 'Rebecca', 'last': 'Kaimbay'}
]

first_names = list(map(lambda fname: fname['first'], names))
print(first_names)

print("========================================")
last_names = list(map(lambda lname: lname['last'], names))
print(last_names)

print("========================================")
def doubles(x): return x*2
print(doubles(3))

print("========================================")
double = map(doubles ,nums)
print(list(double))

print("========================================")
doubl = list(map(lambda x: x*2 ,nums))
print(doubl)