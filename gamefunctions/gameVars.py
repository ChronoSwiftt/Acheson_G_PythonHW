from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives
player_lives = 5
computer_lives = 5

total_lives = 5

# let the Ai make choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player=False