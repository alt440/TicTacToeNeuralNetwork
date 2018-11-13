from tictactoePlay import checkWin
"""
For converting to base 5. Result is 13243
1073 = 1 * 625 + 448
 448 = 3 * 125 + 73
  73 = 2 * 25 + 23
  23 = 4 * 5 + 3
   3 = 3 * 1 + 0
"""
# check first commented file (humanAgainstMachine.py) before reading this one.


# this converts a number to its equivalent in base 3. This method is used to generate all possible values of nine
# numbers in base 3 to generate all possible board scenarios (invalid or valid).
def tobase3(number):
    strNumber = str(number) # converts number to string
    remainders = []   # collects remainders as you go through with division
    comparedValueExponent = 0 # to know up to which power of three the number is situated
    while(number!=0): # the number gets decremented until it reaches 0 for the conversion to be made
        while(number >= 3**comparedValueExponent): # find the highest power of 3 that can match the number
            comparedValueExponent+=1
        if comparedValueExponent != 0:
            comparedValueExponent-=1 # to be right below number. starting point.

        while(comparedValueExponent!=-1): # divide every time by a lower power of three and append the result to remainders
            remainders.append(number//(3**comparedValueExponent))
            number%=(3**comparedValueExponent)
            comparedValueExponent-=1

    answer = ''
    for i in range(len(remainders)):
        # attach all the remainders to make the value in power of three
        answer+= str(remainders[i])
    return answer


# this method checks if the game scenario is a valid one, and if it is accepted to enter the data list.
def isOnePlayerWinning(number4GridStr):
    # checks if one and only one player is winning given the grid

    # the board of tic tac toe with empty spaces (2 = empty)
    board = [[2 for y in range(3)] for x in range(3)]

    # calculate, depending of the board, in how many ways X or O is winning in this scenario.
    # For example, at the end of a game, the user could make two tic tac toes at once: one vertical and one horizontal
    # this check is made to know if in a certain scenario, both X and O are winning. If that is the case, the board
    # scenario is rejected.
    countXWins = 0
    countOWins = 0

    # puts the values inside the board array (because parameter is a string containing numbers from 0 to 2)
    for i in range(3):
        for j in range(3):
            board[i][j]=int(number4GridStr[i])

    # check the winning condition at every space for both O and X. Add 1 if the position is a winning one
    for i in range(9):
        if checkWin(i//3, i%3, 1, board):
            countXWins+=1
        elif checkWin(i//3, i%3, 0, board):
            countOWins+=1

    #limit the possibility to two wins of 1 player at the same time, because for three AI would be dumb
    if (countXWins<=2 and countOWins == 0) or (countOWins<=2 and countXWins == 0):
        return True
    else:
        return False


# evaluates if the grid is possible by looking at the number of Xs versus the number of Os.
def isGridPossible(number4Grid):
    number4GridString = str(number4Grid)

    # padding with zeros if there arent 9 digits, because, say, 111 is not a board, but 000000111 is a board scenario.
    while len(number4GridString) != 9:
        number4GridString = '0'+number4GridString

    # now we have to check if the grid is possible
    # counting Xs and Os to verify if possible. Xs are 1s, Os are 0s.
    x=0
    o=0

    # goes through the strings and counts the number of Xs and Os it has.
    for i in range(len(number4GridString)):
        if number4GridString[i] is '1':
            x+=1
        elif number4GridString[i] is '0':
            o+=1

    # for the board to be valid, there must be the same number of Xs and Os on the board, or 1 X more than Os.
    if x<o or x>o+1:
        return False

    # check if one and only one player is winning
    if not isOnePlayerWinning(number4GridString):
        return False

    return True


# do checkwin 3 times to analyze the whole board at points 1,5,9
# CHANGE FILE PARAMETER TO A FOR APPEND IF IT DIDNT COMPLETE
f = open("contents.txt","w")

# testing all combinations of winning
# representing a tictactoe board with base 3 number because of three
# possible states of spaces
# CHANGE INITIAL VALUE IF DIDNT HAVE TIME TO COMPLETE TABLE
i = 0

# 19682 is the greatest number having 9 values in base 3: 222222222
while (i < 19682):
    base3Nb = tobase3(i)

    number4GridString = str(base3Nb)
    # padding with zeros if there arent 9 digits
    while len(number4GridString) != 9:
        number4GridString = '0' + number4GridString

    # once you get base3 number, verify grid is valid
    someBool = isGridPossible(base3Nb)

    # then if valid, put string number into file, with its initial P value: 0.5
    if someBool:
        # thus, this writes to the file the board scenario as a base3 number with an associated original P value of value 0.5
        f.write(number4GridString + ' 0.5\n')
        print(number4GridString+ ' 0.5')
    # print(i)
    i += 1

f.close()