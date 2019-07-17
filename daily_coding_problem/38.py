'''
Problem # 38

Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
You have an N by N board. Write a function that, 
given N, returns the number of possible arrangements 
of the board where N queens can be placed on the board 
without threatening each other, i.e. no two queens 
share the same row, column, or diagonal.
'''

def pretty_print(queens):
    board = []
    for i in range(len(queens)):
        row = ['_'] * len(queens)
        row[queens[i]] = 'Q'
        board.append(' '.join(row))
    return '\n'.join(board)

def can_place_queen(queens, col, N):
    # Check if column is not already occupied
    if not queens:
        return True
    row_id = len(queens)
    # print(queens, col, row_id)
    for i in range(len(queens)):
        if queens[i] == col:
            return False
        if i - queens[i] + N - 1 == row_id - col + N - 1:
            return False
        if i + queens[i] == row_id + col:
            return False
    return True


def dfs(queens, N, ans):
    if len(queens) == N:
        ans.append(pretty_print(queens))
        return
    [dfs(queens + [i], N, ans) for i in range(N) if can_place_queen(queens, i, N)]

def n_queens(N):
    if N <= 3:
        return None
    ans = []
    dfs([], N, ans)
    print(len(ans))
    for each in ans:
        print(each)
        print('\n')

