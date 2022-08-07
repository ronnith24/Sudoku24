# Sudoku24
#### Video Demo: https://youtu.be/FF5z-5pu420
### Description:
Sudoku24 is my take on the classic puzzle Sudoku. Unlike most of the sudoku games out there Sudoku24
randomly genereates a new sudoku board every time you start a new game. The whole application has 2
main parts the gui of the app so that the user can play easily and the Sudoku class which generates the board
finds the solution and everything else related to the actual sudoku puzzle. Hence to separate the two I have
separated the two into different files.

### Technologies used:
Sudoku24 has been made using python and its pygame module.

### Functions of each file:-
- sudokuSolver.py: This file has one class called Sudoku which has all the methods required to create a valid sudoku board. it has solve the method which uses some other helper methods to solve any sucoku board recursively and checks wether a arrangement of numbers is valid or not, that is, it checks wether the solution is unique or not and wether a solution exists. If a solution exists it stores it for use in the actual game. The constructor has code which used the other method to create an actual grid it first solves an empty board with the solve method and due to the random element of the solve method it generates valid complete sudoku every time. Now to make an actual sudoku which can pose a challenge to the player we randomly fill each cell with 0.5 probability to get a initial sudoku board. To this suoku board we add numbers until the solution becomes unique. After this we randomly select cells and remove the number from them if removing it stil results in valid sudoku, that is, the solution is unique. This class also has hint method which return solution for a random unfilled cell. It also implements an update method to update the sudoku grid every time a number is filled by the player and after checking that wheter it is correct or not.

- main.py: The GUI has 4 main scenes the welcome page, the rules page, the main gaming interface and the finish page. The most complex one to make was the maing sudoku grid I had thought of two strategies one in which we control the function of every cell in the grid from the Board class, and the other was to design a tile class which controls its own functionality and just call the method for every tile. The second one appealed to me as it was much less complex we could just write the tile class and use its functions for every tile while in the first one we would have to handle the different parameters for tiles simultaneously which I think is much more complex to code. The other scenes have been implemented in the main pygame loop.
