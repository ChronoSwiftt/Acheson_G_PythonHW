from random import randint
from gamefunctions import gameVars

def winorlose(status):
	# print("called win or lose", status, "\n")
	print("You", status, "! Would you like to play again?")
	choice = input ("Y / N")

	if choice == "Y" or choice == "y":
			global player_lives
			global computer_lives
			global player
			global computer
			gameVars.player_lives = 5
			gameVars.computer_lives = 5
			gameVars.player = False
			gameVars.computer = gameVars.choices[randint(0,2)]

	elif choice == "N" or choice == "n":
			print("You chose quit. Better luck next time!")
			exit()
	else:
			print("Make a valid choice. Yes or No!")
			winorlose(status)
