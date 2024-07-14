# Sets are like formal mathematical sets.
# Sets do not have duplicate values
# Elemets in sets aren't ordered
# You cannot access items in a set by index

s = ({1,2,3,4,5,5})
print(s)

t = set({1,4,5})
print(t)

print(4 in s)

for num in s:
    print(num)

cities = ['Los Angeles', 'Boulder', 'Kyoto', 'Los Angeles', 'Florence', 'Santiago', 'Shangai', 'Boulder', 'San Francisco', 'Oslo', 'Tokyo']
cities = set(cities)
print(cities)
print(len(set(cities)))

#! Set methods

#* add
s.add(7)
print(s)

cities.add("Ankara")
print(cities)

#* remove
cities.remove('Kyoto')
print(cities)


#* discard
cities.discard('Ankara')
print(cities)

#* copy
another_s = s.copy()
print(another_s)

#* clear - removes all elements of the set

#! Set Math
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# set union
print(math_students | biology_students)

# set intersection
print(math_students & biology_students)

