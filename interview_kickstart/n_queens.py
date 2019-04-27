# place N queens on a NxN board such that no two queens threaten each other
import os
import sys


def find_all_arrangements(N):
    res = []

    def has_conflict(board, row, col):
        for r in range(row):
            if board[r] == col:
                return True
            if abs(board[r] - col) == row - r:
                return True
        return False

    def place_queen(board, row):
        # Base case
        if row == N:
            s = []
            for _, col in enumerate(board):
                s.append(''.join(['-'] * col + ['q'] + ['-'] * (N - col - 1)))
            res.append(',\n'.join(s))
            return

        for col in range(N):
            if not has_conflict(board, row, col):
                board[row] = col
                place_queen(board, row + 1)
        return

    # import pdb
    # pdb.set_trace()
    place_queen([None] * N, 0)
    return res


if __name__ == "__main__":
    f = sys.stdout

    n = int(input())

    res = find_all_arrangements(n)
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y))
        f.write("\n")

    f.close()