# check a temperature and output a result

temperature = int(input("input a number between 0 and 100"))

if temperature <= 4:
	print("water is a solid. cuz its frozen")

elif temperature <= 100:
	print("water is liquid")

else:
	print("water is a gas. cuz its boiling")