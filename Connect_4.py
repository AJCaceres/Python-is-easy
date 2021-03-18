def drawField(field):
	for row in range(11):
		if row%2 == 0:
			practicalRow = int(row/2)
			for column in range(13):
				if column%2 == 0:
					practicalColumn = int(column/2)
					if column!=12:
						print(field[practicalColumn][practicalRow], end="")
					else:
						print(field[practicalColumn][practicalRow])
				else:
					print("|", end="")
		else:
			print("-------------")

 # def checkWinnerVertical(field):
 # 	countX = 0
 # 	countO = 0
 # 	winner = False
 # 	for column in range(6):
 # 		field()
 # 		if column == "X":
 # 			countX += 1
 # 			countO = 0
 # 			if countX == 4:
 # 				print("PLAYER:",Player,"WINS!")
 # 				break
 # 		elif column == "O":
 # 			countO += 1
 # 			countX = 0
 # 			if countO == 4:
 # 				print("PLAYER:",Player,"WINS!")
 # 				break
 # 		else:
 # 			break

def winner(board, piece):
	#horizontal
 	for c in range(3):
 		for r in range(7):
 			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
 				return True
 	#vertical
 	for c in range(6):
 		for r in range(4):
 			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
 				return True
 	#diagonal \
 	for c in range(3):
 		for r in range(4):
 			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
 				return True
 	#diagonal /
 	for c in range(3,6):
 		for r in range(3):
 			if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
 			 	return True



currentField =[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
drawField(currentField)
Player = 1
gameOver = False

while not gameOver:
	print("Players turn: ", Player)
	MoveColumn = int(input("Please enter the column\n"))
	if Player ==1:
		for row in range(6):
			if currentField[MoveColumn][5-row] == "X" or currentField[MoveColumn][5-row] == "O":
				row += 1
				if row == 6:
					print("Column is full, enter another column")
					break
			else:
				currentField[MoveColumn][5-row] = "X"
				
				if winner(currentField,"X"):
					print("PLAYER 1 wins!! Congrats!")
					gameOver = True
				Player = 2
				break

	else:
		for row in range(6):
			if currentField[MoveColumn][5-row] == "O" or currentField[MoveColumn][5-row] == "X":
				row += 1
				if row == 6:
					print("Column is full, enter another column")
					break
			else:
				currentField[MoveColumn][5-row] = "O"
				if winner(currentField,"O"):
					print("PLAYER 2 wins!! Congrats!")
					gameOver = True
				Player = 1
				break

	drawField(currentField)