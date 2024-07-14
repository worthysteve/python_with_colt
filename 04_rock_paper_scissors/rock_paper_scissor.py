from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
random_numb = randint(0, 2)
if random_numb == 0:
	computer = "rock"
elif random_numb == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
    print("It's a tie")
elif player == 'rock':
    if computer == 'scissors':
        print("Player wins")
    else:
        print("Computer wins")
elif player == 'paper':
    if computer == 'rock':
        print("Player wins")
    else:
        print("Computer wins")
elif player == 'scissors':
    if computer == 'paper':
        print("Player wins")
    else:
        print("Computer wins")
else:
    print("Something went wrong")