#9 positions

#can place O and X  on any of those nine positions

board = [[3 for y in range(3)] for x in range(3)]

Xplay = True
win = False

def messageWin(Xplay):
    if Xplay:
        print("You Won X!")
    else:
        print("You Won O!")
    global win;
    win= True

def checkWin(row, column, Xplay):
    Xplay=int(Xplay)

    if row == 0 and board[row + 1][column] == int(Xplay) and board[row + 2][column] == int(Xplay):
        messageWin(Xplay)
    elif row == 1 and board[row - 1][column] == int(Xplay) and board[row + 1][column] == int(Xplay):
        messageWin(Xplay)
    elif row == 2 and board[row - 1][column] == int(Xplay) and board[row - 2][column] == int(Xplay):
        messageWin(Xplay)

    # horizontal win
    if column == 0 and board[row][column + 1] == int(Xplay) and board[row][column + 2] == int(Xplay):
        messageWin(Xplay)
    elif column == 1 and board[row][column + 1] == int(Xplay) and board[row][column - 1] == int(Xplay):
        messageWin(Xplay)
    elif column == 2 and board[row][column - 1] == int(Xplay) and board[row][column - 2] == int(Xplay):
        messageWin(Xplay)

    # right diagonal win
    if column == 0 and row == 2 and board[row - 1][column + 1] == int(Xplay) and board[row - 2][column + 2] == int(Xplay):
        messageWin(Xplay)
    elif column == 1 and row == 1 and board[row - 1][column + 1] == int(Xplay) and board[row + 1][column - 1] == int(Xplay):
        messageWin(Xplay)
    elif column == 2 and row == 0 and board[row + 1][column - 1] == int(Xplay) and board[row + 2][column - 2] == int(Xplay):
        messageWin(Xplay)

    # left diagonal win
    if column == 0 and row == 0 and board[row + 1][column + 1] == int(Xplay) and board[row + 2][column + 2] == int(Xplay):
        messageWin(Xplay)
    elif column == 1 and row == 1 and board[row - 1][column - 1] == int(Xplay) and board[row + 1][column + 1] == int(Xplay):
        messageWin(Xplay)
    elif column == 2 and row == 2 and board[row - 1][column - 1] == int(Xplay) and board[row - 2][column - 2] == int(Xplay):
        messageWin(Xplay)



while not win:

    x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

    x = int(x)-1

    row = x//3
    column = x % 3

    if Xplay:
        board[row][column] = 1
        # check winning condition
        checkWin(row, column, Xplay)

    else:
        board[row][column] = 0
        # check winning condition
        checkWin(row, column, Xplay)

    Xplay = not Xplay