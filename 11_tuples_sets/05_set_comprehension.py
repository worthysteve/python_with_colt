set1 = {x: x ** 2 for x in range(10)}
print(set1)

s = {char.upper() for char in 'hello'}
print(s)

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string('Steven')) # false

string = 'hello'

m = len({char for char in string if char in 'aeiou'})
print(m)