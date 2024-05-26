instructor = {
    "name": "Steven",
    "owns_dog": False,
    "fav_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

cat = {
    "name": "blue",
    "age": 3.5, 
    "is_cute": True
}

print(cat)

cat2 = dict(name = 'kitty', age = 0.5)
print(cat2)

print(f"My name is {instructor['name']}")

#! ITERATING OVER A DICTIONARY
for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)

print(instructor.items())

for key, value in instructor.items():
    print(f"Key is {key} and value is {value}")

#! USING in with dictionaries
if "name" in instructor:
    print("There is a name in dictionary")


#! DICTIONARY METHODS

#* copy
d = dict(a=1,b=2,c=3)
print(d)

clone = d.copy()
print(clone)

print(clone == d) # True
print(clone is d) # False

#* fromkeys
# creates key-value pairs from comma separated values
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)

#* get
print(instructor.get('name'))

#* pop
# takes a single argument corresponding to key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
print(instructor.pop("owns_dog"))

#* popitem
# Removes a random key in a dictionary
print(instructor.popitem())

#* update
# Update keys and values in a dictionary with another set of key value pairs
first = dict(a=1,b=2,c=3)

person = {"city": "Ankara"}
person.update(instructor)
print(person)

person['name'] = "Daniel"
print(person)

person.update
print(person)