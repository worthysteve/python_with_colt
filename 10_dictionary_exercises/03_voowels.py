# Vowels Dict Exercise
# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.

# Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {vowel: 0 for vowel in "aeiou"}
print(answer)

# Using dict.fromkeys:

answer = dict.fromkeys("aeiou", 0) 
print(answer)
