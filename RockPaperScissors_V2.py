# Rock paper scissors console game, play against your computer | Version 2.
# Use functions
import random

options = ["rock", "paper", "scissors"]
gestures = ["👊", "✋", "✌️"]

def play_game():
    game_on = True
    round = 0
    score_board = [0, 0, 0]
    print("Welcome to the rock paper scissors console game!")
    while game_on:
        round += 1
        print("Round " + str(round))
        print("-----------------------")
        score = play_round()
        # score_board = score_board + score; print(score_board) # This line adds elements of the two lists in one , does not do element-wise summation :)
        score_board = [sum(i) for i in zip(score, score_board)]  
        # print(score_board)
        game_on = play_again()
        print("\nSCORE -> Player " + str(score_board[0]) + " : " + str(score_board[1]) + " Computer \n")

        # print("Score " + str(score_board[0]) + " : " + str(score_board[1]) + "\n")
    print("Thanks for playing!")

def play_round():
    player = ""
    computer = random.choice(options)
    while player not in options:
        player = input("What's your pick? Rock, paper, scissors shoot! ").lower()
        for option in options:
            if option.startswith(player):
                player = option
    score = determine_score(computer, player)
    return score

def play_again():
    again = input("Type yes to go for another round! ")
    if again.lower() == "y" or again.lower() == "yes":
        return True
    else:
        return False

def determine_score(computer, player):
    score = [0, 0, 0] #win, loss, tie
    if player == computer:
        score[2] += 1
        print("It's a tie, you both selected " + player + ".")
    elif (player == "rock" and computer != "paper") or (player == "paper" and computer != "scissors") or (player == "scissors" and computer != "rock"):
        score[0] += 1
        print("You won! The computer picked " + computer + ".\n" + player.capitalize() + " beats " + computer + ".")
    else:
        score[1] += 1
        print("You lost! The computer picked " + computer + ".\n" + computer.capitalize() + " beats " + player + ".")
    emojis = gestures[options.index(player)] + " " + gestures[options.index(computer)]
    print(emojis)
    return score

play_game()
