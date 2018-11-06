from tictactoePlay import messageWin
from tictactoePlay import checkWin
from random import randint

def saveToFiles(contentXPVal, contentXBoard, contentOPVal, contentOBoard):
    fileO = open("contentsO2.txt", "w")
    fileX = open("contentsX2.txt", "w")

    # since all the files have the same number of boards, put them all in same for loop
    for i in range(len(contentOBoard)):
        fileO.write(str(contentOBoard[i])+' '+str(contentOPVal[i])+'\n')
        fileX.write(str(contentXBoard[i])+' '+str(contentXPVal[i])+'\n')

    fileO.close()
    fileX.close()

def play():
    turnsBeforeRandomizedMove = 0
    turns = 0

    alphaValue = 0.5  # decreases a little every time a game is played
    decreasingValue = 0.000001  # the decrease amount of the alpha value after every game
    fileO = open("contentsO2.txt", "r")
    fileX = open("contentsX2.txt", "r")

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

    while alphaValue > 0.1:
        # at the beginning of each game initialize those values
        # will represent the current board (nine 2s stands for an empty board. 1 is X, 0 is O
        currentboard = list('222222222')

        # record the previous moves of the player to, after the games, increase/decrease their values. Records indexes of states of games
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

                # X PLAYS RANDOM
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
                        print(''.join(currentboard) + ' DRAW! XRAND')

                    if not draw:
                        count2 = -1
                        indexChanged = 0
                        for i in range(0, len(currentboard)):
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
                                                                                      contentXPval[movesMadeX[n + 1]] -
                                                                                      contentXPval[
                                                                                          movesMadeX[n]])
                                        print('values registered:' + str(contentXPval[movesMadeX[n]]))

                                    for n in range(len(movesMadeO) - 1, -1, -1):
                                        if n == len(movesMadeO) - 1:
                                            contentOPval[movesMadeO[n]] = 0
                                        else:
                                            contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                                          alphaValue * (
                                                                                      contentOPval[movesMadeO[n + 1]] -
                                                                                      contentOPval[
                                                                                          movesMadeO[n]])
                                        print('values registered:' + str(contentOPval[movesMadeO[n]]))

                                    # decrease a little alpha
                                    alphaValue -= decreasingValue
                                break

                            if currentboard[i] is '2':
                                count2 += 1
                                indexChanged = i
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