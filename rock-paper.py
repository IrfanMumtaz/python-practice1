# in this app we will play rock paper sizzor
import random
import sys
# print("0. Rock")
# print("1. Paper")
# print("2. scissors")

x = ["Rock", "Paper", "scissors"]

for i in x:
	print(x.index(i), end="" )
	print(".",i)

player = int(input("Please write a number to select your option: "))
computer = random.randint(0,2)


def checkPlayerChoice(num):
	if(num >= 0 and num <=2):
		print("You chooses", x[player])
		return
	else:
		print("Sorry! you choosed wrong number please restart game")
		sys.exit()

def compareResult(player, computer):
	if(player == computer ):
		print("This game is tied, play again")
		sys.exit()

	elif(player == 0 and computer == 1):
		print("Computer Wins!")
		sys.exit()

	elif(player == 0 and computer == 2):
		print("Player Wins!")
		sys.exit()

	elif(player == 1 and computer == 0):
		print("Player Wins!")
		sys.exit()

	elif(player == 1 and computer == 2):
		print("Computer Wins!")
		sys.exit()

	elif(player == 2 and computer == 0):
		print("Computer Wins!")
		sys.exit()

	elif(player == 2 and computer == 1):
		print("Player Wins!")
		sys.exit()

	else:
		print("This game is tied, play again")
		sys.exit()

checkPlayerChoice(player)

print("Computer choosed", x[computer])

compareResult(player, computer)

