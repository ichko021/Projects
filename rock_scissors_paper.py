#kamuk nojica hartiq
import random

player_1_streak = 0
player_2_streak = 0
choice = ''

def welcome_message():
	print("---ROCK  SCISSORS  PAPER---")
	print("Choose mode: vs COMPUTER or vs PLAYER")
	global choice
	choice = input("(c/p): ")

def player_logic():

	player1 = ''
	player2 = ''

	global player_1_streak
	global player_2_streak


	moves = ['r','s','p']

	player1 = input(f"Choose :{moves} ")
	print(player1)
	global choice
	if choice == "c":
		player2 = random.choice(moves)
		print(player2)
	elif choice == "p":
		for i in range(30):
			print("ANTI-CHEAT SYSTEM")
		player2 = input(f"Choose: {moves} ")
		print(player2)

	

	if player1 == player2:
		print('Tie')
	else:
		if player1 == 'r' and player2 == 's':
			print("Player 1 is winner")
			player_1_streak += 1
		if player1 == 'r' and player2 == 'p':
			print("Player 2 is winner")
			player_2_streak += 1
		if player1 == 's' and player2 == 'r':
			print("Player 2 is winner")
			player_2_streak += 1
		if player1 == 's' and player2 == 'p':
			print("Player 1 is winner")
			player_1_streak += 1
		if player1 == 'p' and player2 == 's':
			print("Player 2 is winner")
			player_2_streak += 1
		if player1 == 'p' and player2 == 'r':
			print("Player 1 is winner")
			player_1_streak += 1

	print(f"Player 1's streak is: {player_1_streak}")
	print(f"Player 2's streak is: {player_2_streak}"	)



def game_loop():

	active = True

	while active:
		choice = input("Do you want to continue?(y/n) ")
		if choice == 'y':
			player_logic()
		else:
			break

welcome_message()
if choice == "c":
	player_logic()
	game_loop()
elif choice == "p":
	player_logic()
	game_loop()

