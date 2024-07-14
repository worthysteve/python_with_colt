import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
guess = None

# if guess == random_number:
#     print("YAY! You win🏆")
# elif guess > random_number:
#     print("Ouch! Too high")
#     int(input("Guess a number between 1 and 10\n"))
# else: 
#     print("Ouch! Too low")
#     int(input("Guess a number between 1 and 10\n"))
# print(random_number)

while guess != random_number:
    guess = int(input("Guess a number between 1 and 10: "))
    guess = int(guess)
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too High!")
    else:
        print("YOU GOT IT!")
    print(random_number)
    