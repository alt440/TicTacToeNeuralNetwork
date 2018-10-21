#9 positions

#can place O and X  on any of those nine positions

board = [[2 for y in range(3)] for x in range(3)]

Xplay = True
win = False

def messageWin(Xplay):
    if Xplay:
        print("You Won X!")
    else:
        print("You Won O!")
    global win;
    win= True

def checkWin(row, column, Xplay, board):
    Xplay=int(Xplay)

    if row == 0 and board[row + 1][column] == int(Xplay) and board[row + 2][column] == int(Xplay):
        return 1
    elif row == 1 and board[row - 1][column] == int(Xplay) and board[row + 1][column] == int(Xplay):
        return 1
    elif row == 2 and board[row - 1][column] == int(Xplay) and board[row - 2][column] == int(Xplay):
        return 1

    # horizontal win
    if column == 0 and board[row][column + 1] == int(Xplay) and board[row][column + 2] == int(Xplay):
        return 1
    elif column == 1 and board[row][column + 1] == int(Xplay) and board[row][column - 1] == int(Xplay):
        return 1
    elif column == 2 and board[row][column - 1] == int(Xplay) and board[row][column - 2] == int(Xplay):
        return 1

    # right diagonal win
    if column == 0 and row == 2 and board[row - 1][column + 1] == int(Xplay) and board[row - 2][column + 2] == int(Xplay):
        return 1
    elif column == 1 and row == 1 and board[row - 1][column + 1] == int(Xplay) and board[row + 1][column - 1] == int(Xplay):
        return 1
    elif column == 2 and row == 0 and board[row + 1][column - 1] == int(Xplay) and board[row + 2][column - 2] == int(Xplay):
        return 1

    # left diagonal win
    if column == 0 and row == 0 and board[row + 1][column + 1] == int(Xplay) and board[row + 2][column + 2] == int(Xplay):
        return 1
    elif column == 1 and row == 1 and board[row - 1][column - 1] == int(Xplay) and board[row + 1][column + 1] == int(Xplay):
        return 1
    elif column == 2 and row == 2 and board[row - 1][column - 1] == int(Xplay) and board[row - 2][column - 2] == int(Xplay):
        return 1
    return 0


def play():
    while not win:

        x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

        x = int(x)-1

        row = x//3
        column = x % 3

        if Xplay:
            board[row][column] = 1
            # check winning condition
            value = checkWin(row, column, Xplay, board)
            if value ==1:
                messageWin(Xplay)

        else:
            board[row][column] = 0
            # check winning condition
            value = checkWin(row, column, Xplay, board)
            if value == 1:
                messageWin(Xplay)

        Xplay = not Xplay
