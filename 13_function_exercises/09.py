# frequency
# Write a function called frequency. This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(freq, search_term):
    return freq.count(search_term)

print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False)) # 1