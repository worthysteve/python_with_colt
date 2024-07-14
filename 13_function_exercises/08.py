
# is_palindrome
# Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(w):
    word = w.lower().strip()
    return word == word[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert') )# False
print(is_palindrome('amanaplanacanalpanama')) # True
print(is_palindrome('a man a plan a canal Panama'))


# The Bonus Version:
# For the more advanced version that ignores whitespace and capitalization, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings (""). Then, I use the lower() string method to convert the string to be all lowercase (and that way the capitalization is ignored when making the equality comparison later). I save the result to a new variable I call stripped .  Then, I simply check if stripped is a palindrome, using the same logic I did in the previous solution.

def is_palindrome(string):
    stripped = string.replace(" ", "").lower()
    return stripped == stripped[::-1]

print(is_palindrome('a man a plan a canal Panama'))