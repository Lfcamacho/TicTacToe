def is_full(board):

	for i in board:
		if '' in i:
			return False
	return True

def valid(board, row, col):

	return True if board[row][col] == '' else False

def has_won(board):


	if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '':
		return True
	if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != '':
		return True

	for x in range(0,3):

		if board[x][0] == board[x][1] and board[x][0] == board[x][2] and board[x][0] != '':
			return True
		if board[0][x] == board[1][x] and board[0][x] == board[2][x] and board[0][x] != '':
			return True

	return False

def computer():
    pass
