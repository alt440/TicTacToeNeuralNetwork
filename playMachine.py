from tictactoePlay import board
from tictactoePlay import messageWin
from tictactoePlay import checkWin
from random import randint


def play():

    turnsBeforeRandomizedMove = 8
    turns = 0

    alphaValue = 0.5  # decreases a little every time a game is played
    fileO = open("../contentsO.txt", "r")
    fileX = open("../contentsX.txt", "r")



    contentOwithP = [line.rstrip('\n') for line in fileO]


    # keeping only the board
    contentOBoard = []
    # keeping only P value
    contentOPval = []
    for i in range(len(contentOwithP)):
        arraySplit = contentOwithP[i].split( )
        contentOBoard.append(arraySplit[0])
        contentOPval.append(float(arraySplit[1]))

    contentXwithP = [line.rstrip('\n') for line in fileX]

    # keeping only the board
    contentXBoard = []
    # keeping only the P value
    contentXPval = []
    for i in range(len(contentXwithP)):
        arraySplit = contentXwithP[i].split( )
        contentXBoard.append(arraySplit[0])  #as string
        contentXPval.append(float(arraySplit[1]))

    fileO.close()
    fileX.close()

    while alphaValue > 0.1:
        #at the beginning of each game initialize those values
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

            if Xplay:
                # choose move according to X from the contentsX.txt file

                # if turns%turnsBeforeRandomizedMove == 0:
                    # possibilities = currentboard.count('2')
                    # randomMove = randint(0, possibilities-1)


                currentboardReplica = currentboard[:]

                maxPValue = 0
                maxPValueBoard = ''
                maxPIndex = -1 #to modify P value at the end of the game
                positionChanged = 0

                for i in range(len(currentboard)):
                    if currentboard[i] is '2':
                        currentboardReplica[i] = '1'
                        intCurrentBoardReplica = int(''.join(currentboardReplica))
                        #get P value for that new board
                        for j in range(len(contentXBoard)):
                            if intCurrentBoardReplica == int(contentXBoard[j]) and maxPValue < contentXPval[j]:
                                maxPValue = contentXPval[j]
                                maxPValueBoard = contentXBoard[j]
                                maxPIndex = j
                                positionChanged = i
                                break

                        currentboardReplica = currentboard[:]

                    if i == len(currentboard)-1 and maxPIndex == -1: # to declare draw
                        win = True
                        print('DRAW!')

                # update current board
                board[positionChanged//3][positionChanged%3] = 1
                currentboard[positionChanged] = '1'
                # remember move. do join because currentboard is a list
                movesMadeX.append(maxPIndex)
                # check winning condition
                value = checkWin(positionChanged//3, positionChanged%3, Xplay, board)
                if value ==1:
                    messageWin(Xplay)
                    win = True
                    print(''.join(currentboard))
                    # change values of each state of board played for X AND O in contentsX.txt AND contentsO.txt
                    for n in range(len(movesMadeX)-1, -1, -1):
                        if n == len(movesMadeX)-1:
                            contentXPval[movesMadeX[n]]=1
                        else:
                            contentXPval[movesMadeX[n]]=contentXPval[movesMadeX[n]] + \
                                                    alphaValue*(contentXPval[movesMadeX[n+1]]-contentXPval[movesMadeX[n]])
                            # print('values registered:'+str(contentXPval[movesMadeX[n]]))

                    for n in range(len(movesMadeO)-1, -1, -1):
                        if n == len(movesMadeO)-1:
                            contentOPval[movesMadeO[n]]=0
                        else:
                            contentOPval[movesMadeO[n]]=contentOPval[movesMadeO[n]] + \
                                                    alphaValue*(contentOPval[movesMadeO[n+1]]-contentOPval[movesMadeO[n]])
                            # print('values registered:' + str(contentOPval[movesMadeO[n]]))

                    #decrease a little alpha
                    alphaValue -= 0.05


            else:
                # choose move according to O from the contextO.txt file
                currentboardReplica = currentboard[:]

                maxPValue = 0
                maxPValueBoard = ''
                maxPIndex = -1  # to modify P value at the end of the game
                positionChanged = 0

                for i in range(len(currentboard)):
                    if currentboard[i] is '2':
                        currentboardReplica[i] = '0'
                        intCurrentBoardReplica = int(''.join(currentboardReplica))
                        # get P value for that new board
                        for j in range(len(contentOBoard)):
                            if intCurrentBoardReplica == int(contentOBoard[j]) and maxPValue < contentOPval[j]:
                                maxPValue = contentOPval[j]
                                maxPValueBoard = contentOBoard[j]
                                maxPIndex = j
                                positionChanged = i
                                break

                        currentboardReplica = currentboard[:]

                    if i == len(currentboard)-1 and maxPIndex == -1: # to declare draw
                        win = True
                        print('DRAW!')

                # update current board
                board[positionChanged // 3][positionChanged % 3] = 0
                currentboard[positionChanged]='0'
                # remember move. do join because currentboard is a list
                movesMadeO.append(maxPIndex)
                # check winning condition
                value = checkWin(positionChanged // 3, positionChanged % 3, Xplay, board)
                if value == 1:
                    messageWin(Xplay)
                    win = True
                    # change values of each state of board played for X AND O in contentsX.txt AND contentsO.txt
                    for n in range(len(movesMadeX) - 1, -1, -1):
                        if n == len(movesMadeX) - 1:
                            contentXPval[movesMadeX[n]] = 0
                        else:
                            contentXPval[movesMadeX[n]] = contentXPval[movesMadeX[n]] + \
                                                      alphaValue * (contentXPval[movesMadeX[n + 1]] - contentXPval[
                            movesMadeX[n]])
                            # print('values registered:'+str(contentXPval[movesMadeX[n]]))

                    for n in range(len(movesMadeO) - 1, -1, -1):
                        if n == len(movesMadeO) - 1:
                            contentOPval[movesMadeO[n]] = 1
                        else:
                            contentOPval[movesMadeO[n]] = contentOPval[movesMadeO[n]] + \
                                                      alphaValue * (contentOPval[movesMadeO[n + 1]] - contentOPval[
                            movesMadeO[n]])
                            # print('values registered:' + str(contentOPval[movesMadeO[n]]))

                    # decrease a little alpha
                    alphaValue -= 0.05

            Xplay = not Xplay
            turns+=1

play()