names = ['Steven', 'Umu', 'Austin', 'Abubakarr']

a_names = filter(lambda n: n[0] == 'A', names)

print(list(a_names))

names = ['Lassie', 'Colt', 'Rusty']
print(list(map(lambda name: f"Your instructor is {name}",
         filter(lambda value: len(value) < 5, names)))) # prints the instructor whose name is below 5 chasracers

# with list comprehension
print([f"Your instructor is {name}" for name in names if len(name) < 5])
