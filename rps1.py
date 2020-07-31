#In this game, Computer and User plays choosing between Rock, Paper and Scissors. Each choice is compared between them. According to the rule, comebody wins.

from random import randint
list1 = ["ROCK", "PAPER", "SCISSORS"]
dictionary1 = {"tie" : "Yawn it's a tie!", "won" : "Yay you won!", "lost": "Aww you lost!"}

def play_game():
    user_choice = input("Enter Rock, Paper or Scissors: ")
    #user_choice = user_choice.upper()
    computer_choice = list1[randint(0,2)]
    decide_winner(user_choice, computer_choice)


def decide_winner(user_choice, computer_choice):
    print ("You selected: %s" % user_choice)
    print ("Computer selected: %s" % computer_choice)
    if user_choice == computer_choice:
        print (dictionary1["tie"])
    elif user_choice == list1[0] and computer_choice == list1[2]:
        print (dictionary1["won"])
    elif user_choice == list1[1] and computer_choice == list1[0]:
        print (dictionary1["won"])
    elif user_choice == list1[2] and computer_choice == list1[1]:
        print (dictionary1["won"])
    else:
        print (dictionary1["lost"])


play_game()



