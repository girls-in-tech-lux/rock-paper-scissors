# Rock paper scissors console game, play against your computer | Version 1.
import random
print("Welcome to the rock paper scissors console game!")
options = ["rock", "paper", "scissors"]
gestures = ["👊", "✋", "✌️"]
computer = ""
player = ""
game_on = True
round = 0
wins = 0 # player's wins = computer's losses
losses = 0 # player's losses = computer's wins
ties = 0 # computer, player
while game_on:
    round += 1
    print("Round " + str(round))
    print("-----------------------")
    computer = random.choice(options)
    while player not in options:
        player = input("What's your pick? Rock, paper, scissors shoot! ").lower()
        for option in options:
            if option.startswith(player):
                player = option
    if player == computer:
        ties += 1
        print("It's a tie, you both selected " + player + ".")
    elif (player == "rock" and computer != "paper") or (player == "paper" and computer != "scissors") or (player == "scissors" and computer != "rock"):
        wins += 1
        print("You won! The computer picked " + computer + ".\n" + player.capitalize() + " beats " + computer + ".")
    else:
        losses += 1
        print("You lost! The computer picked " + computer + ".\n" + computer.capitalize() + " beats " + player + ".")
    emojis = gestures[options.index(player)] + " " + gestures[options.index(computer)]
    print(emojis)
    again = input("Type yes to go for another round! ")
    if again.lower() == "y" or again.lower() == "yes":
        game_on = True
        player = ""
    else:
        game_on = False
    print("SCORE ->  Player " + str(wins) + " : " + str(losses) + " Computer \n")
print("Thanks for playing!")