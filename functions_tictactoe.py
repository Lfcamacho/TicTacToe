import copy
import random

# check if the board is full for ending game
def is_full(board):
    for i in board:
        if '' in i:
            return False
    return True

# check if the actual position is valid
def valid(board, row, col):
    return True if board[row][col] == '' else False

# returns if someone has won or if it's a tie
def has_won(board):
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '':
        return "win"
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != '':
        return "win"

    for x in range(0,3):
        if board[x][0] == board[x][1] and board[x][0] == board[x][2] and board[x][0] != '':
            return "win"
        if board[0][x] == board[1][x] and board[0][x] == board[2][x] and board[0][x] != '':
            return "win"

    if is_full(board):
        return "tie"

    return False

# main function for computer move
def computer(board):
    # recursive function for choosing the best position aplying MiniMax Algorithm
    def best_move(board, turn):
        min_score = 1
        max_score = -1
        pos = [0,0]

        # Change turn
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

        # nested loop for trying every free positions
        for row in range(0,3):
            for col in range(0,3): 
                if valid(board, row, col):
                    boardcopy = copy.deepcopy(board)
                    board[row][col] = turn
                    state = has_won(board)

                    if state:
                        if state == "win":
                            if turn == 'x':                         # if there is a win and its computer's turn return position and max score
                                max_score, pos = 1, [row,col]
                                return [max_score, pos]
                            else:
                                min_score = - 1                     # if there is a win and its person's turn return position and min score
                                return [min_score, pos]
                        else:
                            if turn == 'x' and max_score == -1:
                                max_score, pos = 0, [row,col]
                            if turn == 'o' and max_score == 1:
                                min_score = 0               
                    else:
                        score, pos2 = best_move(board,turn)
                        board = boardcopy
                        if score > max_score:
                            max_score, pos = score, [row,col]
                        if score < min_score:
                            min_score = score
                

        return [max_score, pos] if turn == 'x' else [min_score, pos]    # if finishes comparing all positions in branch max score if it's computers turn, else min score

    # random move in any corner if computer starts playing 
    if board == [['', '', ''],['', '', ''],['', '', '']]:
        return random.choice([[0,0], [2,0], [0,2], [2,2]])
    else:
        turn = 'o'
        a = best_move(board, turn)
        position = a[1]
        return [position[0], position[1]]
