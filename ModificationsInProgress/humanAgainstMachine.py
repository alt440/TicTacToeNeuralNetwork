from tictactoePlay import checkWin
from tictactoePlay import messageWin
import sys

fileO = open("contentsO2.txt", "r")

contentOwithP = [line.rstrip('\n') for line in fileO]


# keeping only the board
contentOBoard = []
# keeping only P value
contentOPval = []
for i in range(len(contentOwithP)):
    arraySplit = contentOwithP[i].split( )
    contentOBoard.append(arraySplit[0])
    contentOPval.append(float(arraySplit[1]))

win = False
board = [[2 for y in range(3)] for x in range(3)]

currentboard = list('222222222')

Xplay = True

while not win:

    if Xplay:
        if currentboard.count('2')==0:
            draw = True
            print('DRAW!')
            break

        x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

        x = int(x) - 1

        row = x // 3
        column = x % 3

        while currentboard[x] != '2':
            x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

            x = int(x) - 1

            row = x // 3
            column = x % 3

        board[row][column] = 1
        # need to modify current board after a move from user
        # also need to verify validity
        currentboard[x] = '1'
        # check winning condition
        value = checkWin(row, column, Xplay, board)
        if value ==1:
            messageWin(Xplay)

    else:

        # choose move according to O from the contextO.txt file
        currentboardReplica = currentboard[:]
        draw = False
        maxPValue = 0
        maxPValueBoard = ''
        maxPIndex = -1  # to modify P value at the end of the game
        positionChanged = -1

        for i in range(0, len(currentboard)):
            if currentboard[i] is '2':
                currentboardReplica[i] = '0'
                intCurrentBoardReplica = int(''.join(currentboardReplica))
                # get P value for that new board
                for j in range(0, len(contentOBoard)):
                    if intCurrentBoardReplica == int(contentOBoard[j]) and maxPValue < contentOPval[j]:
                        maxPValue = contentOPval[j]
                        maxPValueBoard = contentOBoard[j]
                        maxPIndex = j
                        positionChanged = i
                        break

                currentboardReplica = currentboard[:]

            elif i == len(currentboard) - 1 and maxPIndex == -1:  # to declare draw
                win = True
                draw = True
                print(''.join(currentboard) + ' DRAW! OLOG')
                break

        if not draw and positionChanged != -1:
            # update current board
            board[positionChanged // 3][positionChanged % 3] = 0
            currentboard[positionChanged] = '0'
            print('OLOG move position ' + str(positionChanged))
            # check winning condition
            value = checkWin(positionChanged // 3, positionChanged % 3, Xplay, board)
            if value == 1:
                messageWin(Xplay)
                win = True
                print(''.join(currentboard) + ' OLOG')

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                sys.stdout.write('O')
            elif board[i][j]==1:
                sys.stdout.write('X')
            elif board[i][j]==2:
                sys.stdout.write(' ')
            if j != len(board[0])-1:
                sys.stdout.write(' | ')
        print()
    Xplay = not Xplay
