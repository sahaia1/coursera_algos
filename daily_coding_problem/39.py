'''
Problem # 39

Good morning! Here's your coding interview problem for today.
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
Each cell is either dead or alive, and at each tick, the following rules apply:
•	Any live cell with less than two live neighbours dies.
•	Any live cell with two or three live neighbours remains living.
•	Any live cell with more than three live neighbours dies.
•	Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting
list of live cell coordinates and the number of steps it should run for. Once initialized, 
it should print out the board state at each step. Since it's an infinite board, 
print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

# One Step
# O(m*n) space solution using a copy of the original board

import copy

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def check_live_neighbours(row, col, b):
            n = [1, -1, 0]
            rows = len(b)
            cols = len(b[0])
            live_count = 0
            for i in n:
                for j in n:
                    if not (i == 0 and j == 0):
                        n_row = row + i
                        n_col = col + j
                        if 0 <= n_row < rows and 0 <= n_col < cols:
                            # print(row, col, n_row, n_col)
                            live_count += b[n_row][n_col]
            return live_count
             
            
        board_copy = copy.deepcopy(board)
        
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_count = check_live_neighbours(i, j, board_copy)
                # print(i, j, live_count)
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = 0
                if board[i][j] == 0 and live_count == 3:
                    board[i][j] = 1
        

# O(1) space solution

class Solution2:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def check_live_neighbours(row, col, b):
            n = [1, -1, 0]
            rows = len(b)
            cols = len(b[0])
            live_count = 0
            for i in n:
                for j in n:
                    if not (i == 0 and j == 0):
                        n_row = row + i
                        n_col = col + j
                        if 0 <= n_row < rows and 0 <= n_col < cols:
                            # print(row, col, n_row, n_col)
                            live_count += abs(b[n_row][n_col]) == 1
            return live_count
        
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_count = check_live_neighbours(i, j, board)
                # print(i, j, live_count)
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        