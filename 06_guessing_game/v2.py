import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guess = int(guess)
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too High!")
    else:
        print("YOU GOT IT!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
          random_number = random.randint(1,10)  # numbers 1 - 10
          guess = None  
        else:
            print("Thank you for plaing")
            break
print(random_number)
    