from gamefunctions import gameVars
def compareChoices(player):
	if player == gameVars.computer:
		#we have a tie, no point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You Lose!",gameVars.computer,"covers",player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!",player,"smashses",gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You Lose!",gameVars.computer,"cuts",player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!",player,"covers",gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You Lose!",gameVars.computer,"smashes",player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!",player,"cuts",gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1