# TicTacToeNeuralNetwork

Creating an AI using the reinforcement machine learning process. 

A class is made for a normal tic tac toe game. It is made to understand how a normal 2 player tic tac toe game.

Another class is made to get the data set of all possible scenarios in a tic tac toe game. These scenarios will then be associated with a number from 0 to 1, where 1 is the most favorable and 0 the least favorable position of the AI. 

A third class is made to train the AI. It will train the AI with itself to start determining the values associated with the different scenarios.

A final class is made to play against the AI.

I used a report from someone else's project, which is given as a pdf in the repository.

# How to use it

The file "humanAgainstMachine.py" must be executed. It runs on the data list contentO2.txt, which is a file that was specifically 
designed for the player having the Os. When the program is run, it will ask the user to input a number from 1 to 9, which are the
possible locations of where the O piece can go. The position 1 is the top left position and the position 9 is the bottom right position. After each turn, your move along with the move of the AI will get displayed.

The file "dataList.py" was used to generate the list which will be used when playing against the machine. It generates some
6000 possibilities.

The file "randomPlayMachine.py" is to train the AI to know which moves are the best depending on different scenarios. The file "playMachine.py" was previously used to build on the logic of the AI, but since the AI chooses moves that made it win in the first place, then it is unlikely that it will test all possibilities. Thus, making each move random is preferable.

The file "tictactoePlay.py" is the basic tic tac toe game that you play with another player. It does not include an AI.
