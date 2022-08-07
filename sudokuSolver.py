"""
author: Ronnith Nandy
"""

import numpy as np
import random

POSSIBILITIES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Sudoku(object):
    def get_random_position(self, state):
        """
        Input: state a boolean value
        Returns: returns a random empty position if state = True else it returns a filled position
        """
        while True:
            r = random.randrange(9)
            c = random.randrange(9)
            if (self.grid[r, c] == 0) == state:
                break
            
        return (r, c)
    
    def __init__(self):
        self.grid = np.zeros((9, 9), dtype="int32")
        self.solved = False
        self.solve()
        self.get_random_sudoku()
        while True:
            error = self.solve()
            if error == 0:
                break
            if error == 1:
                (r, c) = self.get_random_position(True)
                self.grid[r, c] = self.solution[r, c]
        for i in range(10):
            (r, c) = self.get_random_position(False)
            self.grid[r, c] = 0
            solution = self.solution.copy()
            if self.solve() != 0:
                self.grid[r, c] = solution[r, c]
                self.solution = solution
        if np.sum(self.grid != 0) == 81:
            self.solved = True


    def get_random_sudoku(self):
        """
        Input: None
        Returns: initializes grid to a random sudoku
        """
        for i in range(9):
            for j in range(9):
                if random.randint(1, 10) > 5:
                    self.grid[i, j] = self.solution[i, j]
                else:
                    self.grid[i, j] = 0
    
    def is_partially_valid(self, grid):
        """
        Input: A numpy array which contains a sudoku
        Returns: True if the no. till now do not violate any of the sudoku rules else False
        """
        for i in range(9):
            values = {}
            for j in range(9):
                if grid[i, j] == 0:
                    continue
                if values.get(grid[i, j]):
                    return False
                values[grid[i, j]] = True
                
        for j in range(9):
            values = {}
            for i in range(9):
                if grid[i, j] == 0:
                    continue
                if values.get(grid[i, j]):
                    return False
                values[grid[i, j]] = True
                
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                values = {}
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if grid[i, j] == 0:
                            continue
                        if values.get(grid[i, j]):
                            return False
                        values[grid[i, j]] = True
        
        return True
    
    def solve(self):
        """
        Input: None
        Returns: solves the generated sudoku and stores the solution
        """
        solution = self.grid.copy()
        self.counter = 0
        self.recursive_solve(solution)
        if self.counter == 0:
            return -1
        elif self.counter == 1:
            return 0
        else:
            return 1
    
    def recursive_solve(self, solution, x=0, y=0):
        if x == 9:
            self.solution = solution.copy()
            self.counter += 1
            if self.counter > 1:
                return True
            else:
                return False

        (nxt_x, nxt_y) = (x, y)
        if y == 8:
            nxt_x += 1
            nxt_y = 0
        else:
            nxt_y += 1

        if solution[x, y] != 0:
            return self.recursive_solve(solution, nxt_x, nxt_y)
        
        for number in random.sample(POSSIBILITIES, 9):
            solution[x, y] = number
            if self.is_partially_valid(solution):
                terminate = self.recursive_solve(solution, nxt_x, nxt_y)
                if terminate:
                    return False
            solution[x, y] = 0
            
    
    def update(self, i, j, number):
        """
        Input: Index of row and column in order along with users guess
        Returns: True if it is correct or else False
        """
        if self.solution[i, j] == number:
            self.grid[i, j] = number
            if np.sum(self.grid != 0) == 81:
                self.solved = True
            return True
        return False
    
    
    def get_solution(self, i, j):
        """
        Input: index of cell as two pairs of integers i is row and j is column
        Returns: The required number at that point
        """
        return self.solution[i, j]
    
    
    def hint(self):
        """
        Input: None
        Returns: The cell and number in it as hint if the sudoku is not already solved else return -1.
        """
        if self.solved:
            return -1
        
        (r, c) = self.get_random_position(True)
        self.grid[r, c] = self.solution[r, c]
        
        return (r, c, self.solution[r, c])
    
    def __str__(self):
        result = ""
        for i in range(9):
            for j in range(9):
                result =  result + " " + str(self.grid[i, j])
            result =  result + '\n'
        return result
