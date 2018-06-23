#guess the hidden number game

import random, sys


attempts = 7
while(attempts > 0):
	hiddenNumber = random.randint(0,100)
	num = int(input("Please guess a number between 0 to 100, you have 7 attempts. "))


	def restartGame():
		again = input("Do you want to play again? Y/N ")

		if(again == "Y" or again == "y"):
			attempts = 7
		else:
			attempts = 0
			sys.exit()


	def greaterOrSmall(guess, hidden, attempts):
		if(guess < hidden):
			print("Your number is smaller than hidden number, you have %d attempts left" % attempts)
			return
		else:
			print("Your number is greater than hidden number, you have %d attempts left" % attempts)
			return


	def checkNumber(guess, hidden, attempts):
		if(guess == hiddenNumber):
			print("Congratulations you won, hidden number is", hiddenNumber)
			restartGame()
		else:
			attempts = attempts - 1
			if(attempts > 0):
				greaterOrSmall(guess, hiddenNumber, attempts)
				num = int(input("Please guess another number: "))
				checkNumber(num, hidden, attempts)

			else:
				print("You have %d attempts left, You have lost." % attempts)
				restartGame()

				

	checkNumber(num, hiddenNumber, attempts)