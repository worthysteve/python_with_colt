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