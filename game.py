
from random import randint
from gamefunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("======================================")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("======================================")
	print("Choose your Weapon\n")
	player=input("choose rock, paper or scissors:")
	compare.compareChoices(player)
	# start doing some logic and condition checking
	# print("computer:", computer, "player:", player)
	
	if gameVars.player_lives == 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		 winlose.winorlose("won")

	else:
		 player = False
		 gameVars.computer=gameVars.choices[randint(0,2)]


