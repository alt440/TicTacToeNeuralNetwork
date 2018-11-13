from tictactoePlay import messageWin
from tictactoePlay import checkWin
from random import randint
# please read humanAgainstMachine.py before trying to understand this file

# NOTE: A P value of 1 is an always winning scenario. A P value of 0 is an always losing scenario.

# to save the modifications brought to these arrays (parameters) into files
def saveToFiles(contentXPVal, contentXBoard, contentOPVal, contentOBoard):
    fileO = open("contentsO2.txt", "w")
    fileX = open("contentsX2.txt", "w")

    # since all the files have the same number of boards, put them all in same for loop
    for i in range(len(contentOBoard)):
        # look at dataList.py comments to understand the structure of the input to files
        fileO.write(str(contentOBoard[i])+' '+str(contentOPVal[i])+'\n')
        fileX.write(str(contentXBoard[i])+' '+str(contentXPVal[i])+'\n')

    # close the file to write the changes
    fileO.close()
    fileX.close()

def play():

    # turns left before the move gets randomized. In this case, every turn is random.
    turnsBeforeRandomizedMove = 0
    turns = 0

    # the alpha value indicates the degree of the change of the P values at the end of the game.
    alphaValue = 0.5  # decreases a little every time a game is played
    decreasingValue = 0.000001  # the decrease amount of the alpha value after every game
    fileO = open("contentsO2.txt", "r")
    fileX = open("contentsX2.txt", "r")

    # look at the comments of humanAgainstMachine.py if this is not understood
    contentOwithP = [line.rstrip('\n') for line in fileO]

    # keeping only the board
    contentOBoard = []
    # keeping only P value
    contentOPval = []
    for i in range(len(contentOwithP)):
        arraySplit = contentOwithP[i].split()
        contentOBoard.append(arraySplit[0])
        contentOPval.append(float(arraySplit[1]))

    contentXwithP = [line.rstrip('\n') for line in fileX]

    # keeping only the board
    contentXBoard = []
    # keeping only the P value
    contentXPval = []
    for i in range(len(contentXwithP)):
        arraySplit = contentXwithP[i].split()
        contentXBoard.append(arraySplit[0])  # as string
        contentXPval.append(float(arraySplit[1]))

    fileO.close()
    fileX.close()

    # play until the alpha value is equal or smaller to 0.1 (this can happen because the decreasing value decreases the
    # alphaValue after each game)
    while alphaValue > 0.1:
        # at the beginning of each game initialize those values
        # will represent the current board (nine 2s stands for an empty board. 1 is X, 0 is O
        currentboard = list('222222222')

        # record the previous moves of the player to, after the games, increase/decrease their values.
        # Records indexes of states of games (records indexes in the arrays contentOBoard and contentXBoard of the
        # board scenarios the AI chose to play to affect their P values at the end of the game)
        movesMadeX = []
        movesMadeO = []

        # reinitialize board
        board = [[2 for y in range(3)] for x in range(3)]

        # for X to start
        Xplay = True

        # for game to relaunch
        win = False

        while not win:

            # X PLAYS
            if Xplay:
                # choose move according to X from the contentsX.txt file

                # X PLAYS RANDOM, which is always true in this case as the if condition states
                if True:
                    draw = False
                    # calculating the number of possibilities the AI has
                    possibilities = currentboard.count('2')
                    if possibilities > 1:
                        # the move is chosen at random. the move will affect the i'th 2 value (the 2 that is placed
                        # randomMove'th)
                        randomMove = randint(0, possibilities - 1)
                    elif possibilities == 1:
                        # then only one move can be played
                        randomMove = 0
                    else:
                        # if the game is a draw
                        draw = True
                        win = True
                        # alpha value is decreased, no change in P values is performed
                        alphaValue -= decreasingValue
                        print(''.join(currentboard) + ' DRAW! XRAND')

                    if not draw:
                        # number of 2s passed. this is used to compare to the value randomMove, because randomMove indicates
                        # which 2 is going to get changed
                        count2 = -1

                        # the index that will be changed
                        indexChanged = 0

                        # going through the whole board
                        for i in range(0, len(currentboard)):

                            # when we reach the randomMove'th 2
                            if count2 == randomMove:
                                # then we change its value to 1, because we are X that are making the move
                                currentboard[indexChanged] = '1'
                                # change as well the value on the board array
                                board[indexChanged // 3][indexChanged % 3] = 1
                                print('XRAND move position ' + str(indexChanged))
                                # search for index of board in contentXBoard list
                                indexBoard = -1
                                # transform the current board to an int to facilitate comparison
                                intCurrentBoard = int(''.join(currentboard))

                                # search for the index of the corresponding board to possibly modify its P value at the
                                # end of the game
                                for j in range(0, len(contentXBoard)):
                                    if intCurrentBoard == int(contentXBoard[j]):
                                        indexBoard = j
                                        break

                                # the index is added to movesMadeX to modify its P value at the end of the game if any
                                # party wins
                                movesMadeX.append(indexBoard)

                                # checks if that last move played generated a win for the player X
                                value = checkWin(indexChanged // 3, indexChanged % 3, Xplay, board)

                                # if checkWin returns 1, player X has won
                                if value == 1:
                                    # returns the message for the win
                                    messageWin(Xplay)
                                    win = True
                                    print(''.join(currentboard) + ' XRAND')

                                    # change values of each state of board played (or board scenario played) for X AND
                                    # O in contentsX.txt AND contentsO.txt
                                    # start from the highest n and go down to 0 (for X)
                                    for n in range(len(movesMadeX) - 1, -1, -1):
                                        if n == len(movesMadeX) - 1:
                                            # because X has won, the P value for the last board scenario (the winning
                                            # scenario) is set to 1, because it will always make X win
                                            contentXPval[movesMadeX[n]] = 1
                                        else:
                                            # if the move is not the last one, it could be a losing or winning move
                                            # depending on the circumstances. The formula to determine the P value
                                            # of those board scenarios are currentValue + alphaValue*(nextMove -
                                            # currentValue). Looking at this formula, we notice it takes consideration
                                            # of the previous value and the P value of the move that was played after it
                                            contentXPval[movesMadeX[n]] = contentXPval[movesMadeX[n]] + \
                                                                          alphaValue * (
                                                                                      contentXPval[movesMadeX[n + 1]] -
                                                                                      contentXPval[
                                                                                          movesMadeX[n]])
                                        print('values registered:' + str(contentXPval[movesMadeX[n]]))

                                    # starts from the highest n and goes down to 0 (for O)
                                    for n in range(len(movesMadeO) - 1, -1, -1):
                                        if n == len(movesMadeO) - 1:
                                            # because O has lost, the P value for the last board scenario (the losing
                                            # scenario) is set to 0, because it will always make O lose
                                            contentOPval[movesMadeO[n]] = 0
                                        else:
                                            # if the move is not the last one, it could be a losing or winning move
                                            # depending on the circumstances. The formula to determine the P value
                                            # of those board scenarios are currentValue + alphaValue*(nextMove -
                                            # currentValue). Looking at this formula, we notice it takes consideration
                                            # of the previous value and the P value of the move that was played after it
                                            # Notice the formula to attributes points to the P values of the previous
                                            # board scenarios is the same as X's. This is because we start with a P
                                            # value of 0 from the last move, thus this diminishes the P values of the
                                            # preceding moves.
                                            contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                                          alphaValue * (
                                                                                      contentOPval[movesMadeO[n + 1]] -
                                                                                      contentOPval[
                                                                                          movesMadeO[n]])
                                        print('values registered:' + str(contentOPval[movesMadeO[n]]))

                                    # decrease a little alpha because the game is finished
                                    alphaValue -= decreasingValue
                                break

                            if currentboard[i] is '2':
                                # we want to change the count2 value every time we encounter a 2 in the array
                                count2 += 1
                                # we set the index changed to this new 2 that was encountered
                                indexChanged = i

                                # this below was added in case count2 becomes equal to the randomMove at the last index
                                # because it was the last index, the loop would simply quit before the if condition
                                # just above (if count2 == randomMove) could be operated one last time.
                                # this below has the same behavior as what is in the if condition just above.
                                if i == len(currentboard)-1 and count2 == randomMove:
                                    if count2 == randomMove:
                                        currentboard[indexChanged] = '1'
                                        board[indexChanged // 3][indexChanged % 3] = 1
                                        print('XRAND move position ' + str(indexChanged))
                                        # search for index of board in X list
                                        indexBoard = -1
                                        intCurrentBoard = int(''.join(currentboard))
                                        for j in range(0, len(contentXBoard)):
                                            if intCurrentBoard == int(contentXBoard[j]):
                                                indexBoard = j
                                                break

                                        movesMadeX.append(indexBoard)
                                        value = checkWin(indexChanged // 3, indexChanged % 3, Xplay, board)

                                        if value == 1:
                                            messageWin(Xplay)
                                            win = True
                                            print(''.join(currentboard) + ' XRAND')
                                            # change values of each state of board played for X AND O in contentsX.txt AND contentsO.txt
                                            for n in range(len(movesMadeX) - 1, -1, -1):
                                                if n == len(movesMadeX) - 1:
                                                    contentXPval[movesMadeX[n]] = 1
                                                else:
                                                    contentXPval[movesMadeX[n]] = contentXPval[movesMadeX[n]] + \
                                                                                  alphaValue * (
                                                                                          contentXPval[
                                                                                              movesMadeX[n + 1]] -
                                                                                          contentXPval[
                                                                                              movesMadeX[n]])
                                                print('values registered:' + str(contentXPval[movesMadeX[n]]))

                                            for n in range(len(movesMadeO) - 1, -1, -1):
                                                if n == len(movesMadeO) - 1:
                                                    contentOPval[movesMadeO[n]] = 0
                                                else:
                                                    contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                                                  alphaValue * (
                                                                                          contentOPval[
                                                                                              movesMadeO[n + 1]] -
                                                                                          contentOPval[
                                                                                              movesMadeO[n]])
                                                print('values registered:' + str(contentOPval[movesMadeO[n]]))

                                            # decrease a little alpha
                                            alphaValue -= decreasingValue


            # O PLAYS
            # if you understood the general behavior for choosing moves for X, then this below should be no problem at
            # all. Everything is the same, except to make a move now, the values set in the arrays are 0. Also, if O
            # wins, the values in the contentXPVal are decreased (last move has P value of 0, and previous moves suffer
            # from that low value) and the values in the contentOPVal are increased (last move has P value of 1, and
            # previous moves benefit from that high value)
            elif not Xplay:

                # O PLAYS RANDOM
                if True:
                    draw = False
                    possibilities = currentboard.count('2')
                    if possibilities > 1:
                        randomMove = randint(0, possibilities - 1)
                    elif possibilities == 1:
                        randomMove = 0
                    else:
                        draw = True
                        win = True
                        alphaValue -= decreasingValue
                        print(''.join(currentboard) + ' DRAW! ORAND')

                    if not draw:
                        count2 = -1
                        indexChanged = 0
                        for i in range(0, len(currentboard)):
                            if count2 == randomMove:
                                currentboard[indexChanged] = '0'
                                board[indexChanged // 3][indexChanged % 3] = 0
                                print('ORAND move position ' + str(indexChanged))
                                # search for index of board in X list
                                indexBoard = -1
                                intCurrentBoard = int(''.join(currentboard))
                                for j in range(0, len(contentOBoard)):
                                    if intCurrentBoard == int(contentOBoard[j]):
                                        indexBoard = j
                                        break

                                movesMadeO.append(indexBoard)
                                value = checkWin(indexChanged // 3, indexChanged % 3, Xplay, board)

                                if value == 1:
                                    messageWin(Xplay)
                                    win = True
                                    print(''.join(currentboard) + ' ORAND')
                                    # change values of each state of board played for X AND O in contentsX.txt AND contentsO.txt
                                    for n in range(len(movesMadeO) - 1, -1, -1):
                                        if n == len(movesMadeO) - 1:
                                            contentOPval[movesMadeO[n]] = 1
                                        else:
                                            contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                                          alphaValue * (
                                                                                      contentOPval[movesMadeO[n + 1]] -
                                                                                      contentOPval[movesMadeO[n]])
                                        print('values registered:' + str(contentOPval[movesMadeO[n]]))

                                    for n in range(len(movesMadeX) - 1, -1, -1):
                                        if n == len(movesMadeX) - 1:
                                            contentXPval[movesMadeX[n]] = 0
                                        else:
                                            contentXPval[movesMadeX[n]] = contentXPval[movesMadeX[n]] + \
                                                                          alphaValue * (
                                                                                      contentXPval[movesMadeX[n + 1]] -
                                                                                      contentXPval[movesMadeX[n]])
                                        print('values registered:' + str(contentXPval[movesMadeX[n]]))

                                    # decrease a little alpha
                                    alphaValue -= decreasingValue
                                break

                            if currentboard[i] is '2':
                                count2 += 1
                                indexChanged = i
                                if i == len(currentboard)-1 and count2 == randomMove:
                                    if count2 == randomMove:
                                        currentboard[indexChanged] = '0'
                                        board[indexChanged // 3][indexChanged % 3] = 0
                                        print('ORAND move position ' + str(indexChanged))
                                        # search for index of board in X list
                                        indexBoard = -1
                                        intCurrentBoard = int(''.join(currentboard))
                                        for j in range(0, len(contentOBoard)):
                                            if intCurrentBoard == int(contentOBoard[j]):
                                                indexBoard = j
                                                break

                                        movesMadeO.append(indexBoard)
                                        value = checkWin(indexChanged // 3, indexChanged % 3, Xplay, board)

                                        if value == 1:
                                            messageWin(Xplay)
                                            win = True
                                            print(''.join(currentboard) + ' ORAND')
                                            # change values of each state of board played for X AND O in contentsX.txt AND contentsO.txt
                                            for n in range(len(movesMadeO) - 1, -1, -1):
                                                if n == len(movesMadeO) - 1:
                                                    contentOPval[movesMadeO[n]] = 1
                                                else:
                                                    contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                                                  alphaValue * (
                                                                                          contentOPval[
                                                                                              movesMadeO[n + 1]] -
                                                                                          contentOPval[movesMadeO[n]])
                                                print('values registered:' + str(contentOPval[movesMadeO[n]]))

                                            for n in range(len(movesMadeX) - 1, -1, -1):
                                                if n == len(movesMadeX) - 1:
                                                    contentXPval[movesMadeX[n]] = 0
                                                else:
                                                    contentXPval[movesMadeX[n]] = contentXPval[movesMadeX[n]] + \
                                                                                  alphaValue * (
                                                                                          contentXPval[
                                                                                              movesMadeX[n + 1]] -
                                                                                          contentXPval[movesMadeX[n]])
                                                print('values registered:' + str(contentXPval[movesMadeX[n]]))

                                            # decrease a little alpha
                                            alphaValue -= decreasingValue




            Xplay = not Xplay
            turns += 1

        saveToFiles(contentXPval, contentXBoard, contentOPval, contentOBoard)

play()