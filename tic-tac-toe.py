def welcome():
	print("Welcome to the Tic-Tac-Toe game!")
	print("Click numbers to place a mark")
	print("""
	1 | 2 | 3
	---------
	4 | 5 | 6
	---------
	7 | 8 | 9
	""")

def mark_choice():
	print("Choose a mark (X or O)")
	player1_choice = input("Player 1: ")
	player2_choice = input("Player 2: ")
	return (player1_choice, player2_choice)
		
def make_move(is1, arr):
	field = int(input("Choose a field number (1-9): "))
	
	if is1 == True and arr[field - 1] == " ":
		moves[field - 1] = pl1
		return False
	elif is1 == False:
		moves[field - 1] = pl2
		return True

def draw_board(arr):
	print(f"""
	{arr[0]} | {arr[1]} | {arr[2]} 
	---------
	{arr[3]} | {arr[4]} | {arr[5]}
	---------
	{arr[6]} | {arr[7]} | {arr[8]}
	""")
	
def is_game_ended(arr):
	if " " in arr:
		return False
	else: 
		return True

def is_won(arr, pl):
	if arr[0] == arr[1] == arr[2] == pl or \
	arr[3] == arr[4] == arr[5] == pl or \
	arr[6] == arr[7] == arr[8] == pl or \
	arr[0] == arr[3] == arr[6] == pl or \
	arr[1] == arr[4] == arr[7] == pl or \
	arr[2] == arr[5] == arr[8] == pl or \
	arr[0] == arr[4] == arr[8] == pl or \
	arr[2] == arr[4] == arr[6] == pl:
		return True
	else:
		return False
	
welcome()
play_again = True

while play_again:
	end_of_game = False
	won_game = False
	moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
	pl1, pl2 = mark_choice()	
	is_player1_move = True
	
	while end_of_game == False and won_game == False:
		is_player1_move = make_move(is_player1_move, moves)
		draw_board(moves)
		if is_player1_move == True:
			won_game = is_won(moves, pl2)
			if won_game:
				print("Player 2 won")
		else:
			won_game = is_won(moves, pl1)
			if won_game:
				print("Player 1 won")
		end_of_game = is_game_ended(moves)
		
	yes_or_no = input("End of game. Do you want to play again? (y/n) ")
	if yes_or_no == "y":
		play_again = True
	else:
		play_again = False
