# Accessing List Data
# I'm having a party, and made a list of people I want to invite.  Unfortunately, I'm a terrible friend and made a couple of spelling errors.  Help me correct them!

# Change "Hanna" to "Hannah" (there should be an 'h' at the end)

# Change "Geoffrey" to "Jeffrey"

# Change "aparna" to "Aparna" (capitalize it)

# Hint: You can use the following syntax to change a value of an existing list element at the specific index position:

# lst[0] = "NewValue"

# Here, lst would represent the variable holding the list that we are modifying, and the 0 in square brackets would be the index number of the targetted list element that we are changing, and we would use the assignment operator = to set it to a new value. You can use this approach with the people list in this exercise to make the necessary modifications, as instructed above!
# DON'T TOUCH THIS PLEASE!

people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
people[0] = 'Hannah'
people[-1] = 'Aparna'

print(people)