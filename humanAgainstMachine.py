from tictactoePlay import checkWin
from tictactoePlay import messageWin
import sys

fileO = open("contentsO2.txt", "r")

# take the file line by line
contentOwithP = [line.rstrip('\n') for line in fileO]

# these two arrays are easily associated because the index of a board has the P value of the same index in the
# contentOPval array
# keeping only the board
contentOBoard = []
# keeping only P value
contentOPval = []

# split the P value (score attributed for the scenario) from the board scenario (which is composed of 2s, 1s, and 0s,
# where 0s stand for O, 1s stand for X, and 2s stand for empty spaces in tic tac toe)
for i in range(len(contentOwithP)):
    arraySplit = contentOwithP[i].split( )
    # print(str(arraySplit[0])+" "+str(arraySplit[1]))
    contentOBoard.append(arraySplit[0])
    contentOPval.append(float(arraySplit[1]))

# the board for the tic tac toe game, set with nine 2s, or nine empty spaces (2 = empty space)
board = [[2 for y in range(3)] for x in range(3)]

# currentboard is the current board of the game (starts with a board with only empty spaces)
currentboard = list('222222222')

# Xplay determines who's turn it is. If set to true, then it is X's turn; set to false, it is O's turn.
Xplay = True

# win identifies if the game has been won. If so, we get out of the below loop.
win = False

# while the game has not been won
while not win:

    # if it is Xs turn
    if Xplay:

        # if there are no more empty spaces (no more 2)
        if currentboard.count('2')==0:
            draw = True
            print('DRAW!')
            break

        # asks for user input, as User is X
        x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

        # subtract one because index of array starts at 0
        x = int(x) - 1

        # simple trick to know which row and which column the move belongs to
        row = x // 3
        column = x % 3

        # loop until player inputs a valid location
        while currentboard[x] != '2':
            x = input("Enter your move (from position 1 to 9 on tic tac toe board):")

            x = int(x) - 1

            row = x // 3
            column = x % 3

        # notice there is NO INPUT VALIDATION apart from is the number inputted between 1 to 9
        # this marks the move on the board. 1 is put because the user plays X. For O, this would equal 0 instead.
        board[row][column] = 1

        # need to modify current board after a move from user
        currentboard[x] = '1'

        # check winning condition. This checks if this move has made the user win by checking diagonals/horizontal/vertical
        value = checkWin(row, column, Xplay, board)

        # checkWin returns 1 if the user won
        if value ==1:
            # displays a message showing the user won
            messageWin(Xplay)

    else:

        # the currentboardReplica simulates possible board scenarios to identify which move would be the best
        currentboardReplica = currentboard[:]

        # draw variable, which is set true if the game is a draw (or no more empty spaces)
        draw = False

        # setting starting values: when we are looking for the best move for the AI, we are looking for the best possible
        # scenario, or the best move, by identifying the scenario that has the biggest P value
        maxPValue = 0

        # the board associated with the max P value
        maxPValueBoard = ''

        # the index in the contentOPval array where the P value is
        maxPIndex = -1  # to modify P value at the end of the game

        # the position that has been modified on the board (or the index changed of the board)
        positionChanged = -1

        for i in range(0, len(currentboard)):
            # if the space is free
            if currentboard[i] is '2':
                # try putting a 0 there, because 0 is associated to Os
                currentboardReplica[i] = '0'
                # put the board into an integer to be more easily evaluated later
                intCurrentBoardReplica = int(''.join(currentboardReplica))
                # get P value for that new board (we changed a value at position i because it was free, now we have to
                # search for that new scenario in our contentOBoard list)
                for j in range(0, len(contentOBoard)):
                    # if the board scenario is the same and the P value of that board is superior to the maxPValue
                    # already registered, then we take the information of that board.
                    if intCurrentBoardReplica == int(contentOBoard[j]) and maxPValue < contentOPval[j]:
                        maxPValue = contentOPval[j]
                        maxPValueBoard = contentOBoard[j]
                        maxPIndex = j
                        positionChanged = i
                        break

                # we reset the currentboardReplica array to avoid putting a change, and then putting other changes on
                # top of it. We are searching for the ONE move to make, not a chaining of moves.
                currentboardReplica = currentboard[:]

            # this declares a draw in the case that no board scenario was found: this would execute if no '2' were
            # identified in the currentboard variable
            elif i == len(currentboard) - 1 and maxPIndex == -1:  # to declare draw
                win = True
                draw = True
                print(''.join(currentboard) + ' DRAW! OLOG')
                break

        # this applies a change to the board if a move has been found
        if not draw and positionChanged != -1:
            # update current board with 0, because O is identified as 0
            board[positionChanged // 3][positionChanged % 3] = 0
            currentboard[positionChanged] = '0'
            print('OLOG move position ' + str(positionChanged))
            # check winning condition. See above for more comments
            value = checkWin(positionChanged // 3, positionChanged % 3, Xplay, board)
            if value == 1:
                messageWin(Xplay)
                win = True
                print(''.join(currentboard) + ' OLOG')

    # this is a 'toString' of the board: it prints out the string representation of the board with O,X and empty spaces
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

    # this changes the turn. If X played, then it is O's turn, otherwise it is X turn.
    Xplay = not Xplay
