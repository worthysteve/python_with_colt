
# single_letter_count
# Write a function called single_letter_count. This function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.  

# Hint: take advantage of count() method

'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("Hello World", "h") )# 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l") )# 3