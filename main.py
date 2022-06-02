#Rock,paper and scissors game
#This is a game which allows user to play with a computer

#Note!
#"R" = "Rock"
# "P" = "Paper"
# "S" = "scissors"

import random 

print("Welcome to Rock, Paper, Scissors!")
print("---------------------------------")

while True:
    choices = ["R","P","S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\nPick A Hand. R, P or S:-->").lower().upper()
    if player == computer:
        print("computer:", computer)
        print("player:" , player)
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player : ", player)
            print("Sorry you lost!", computer, "beats", player)
        if computer == "S":
            print("computer: ", computer)
            print("player : ", player)
            print("Congrat! You win", player, "beats", computer )
    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player : ", player)
            print("Sorry You lost!", computer, "beats", player)
        if computer == "P":
            print("computer: ", computer)
            print("player : ", player)
            print("Congrat! You win", player, "beats", computer)
    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player : ", player)
            print("Sorry You lost!", computer, "beats", player)
        if computer == "R":
            print("computer: ", computer)
            print("player : ", player)
            print("Congrat! You win", player, "beats", computer)
        
    play_again = input("play again ? (Yes / No):--> ").lower()

    if play_again != "yes":
      
        break
print("Game over! Thank you for playing : ")
print("Bye!")
    