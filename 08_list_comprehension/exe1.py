# List Comprehension Exercises
# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.  I would use a list comprehension, though you could also loop over manually.

# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  Another good candidate for a list comp.

names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(answer)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in  numbers if num % 2 == 0]
print(answer2)