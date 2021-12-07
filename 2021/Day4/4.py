import numpy as np

def main():
    inputfile = open('input.txt', 'r')
    lines = inputfile.readlines()
    rolls = [role.replace('\n', '') for role in lines[0].split(',')]
    boardlines = lines[2:]
    boards = []
    currentboard = []
    for boardline in boardlines:
        if boardline == '\n':
            boards.append(currentboard)
            currentboard = []
            continue
        else:
            currentboard.append([num for num in boardline.strip().split(' ') if num != '']) 
    for roll in rolls:
        for board in boards:
            board = mark_board(roll, board)
            if check_if_aced(board):
                result = sum([ int(num) for num in np.concatenate(board) if num != 'X'])
                print(result * int(roll))
                return

def mark_board(roll, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == roll:
                board[i][j] = 'X'
    return board

def check_if_aced(board):
    turnedBoard = list(zip(*board))
    for i in range(len(board)):
        if all(x == 'X' for x in board[i]) or all(x == 'X' for x in turnedBoard[i]): 
            return True
    return False

if __name__ == '__main__':
    main()