print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Make your move: ")
player2 = input("Make your move: ")

if player1 == 'rock' and player2 == 'scissors':
    print("Player1 wins")
elif player1 == 'rock' and player2 == 'paper':
    print("Player2 wins")
elif player1 == 'paper' and player2 == 'rock':
    print("Player1 wins")
elif player1 == 'paper' and player2 == 'scissors':
    print("Player2 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("Player1 wins")
elif player1 == 'scissors' and player2 == 'rock':
    print("Player2 wins")
elif player1 == player2:
    print("It's a tie")
else:
    print("Something went wrong")
