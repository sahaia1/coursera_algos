'''
Problem # 23

Daily Coding Problem

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''


def recursive_min_steps(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])

    def recursive(p, steps_so_far):
        if p == end:
            return steps_so_far
        matrix[p[0]][p[1]] = True
        if 0 <= p[0] < rows and 0 <= p[1] - 1 < cols and matrix[p[0]][
                p[1] - 1] == False:
            left = recursive((p[0], p[1] - 1), 1 + steps_so_far)
        else:
            left = float('inf')
        if 0 <= p[0] < rows and 0 <= p[1] + 1 < cols and matrix[p[0]][
                p[1] + 1] == False:
            right = recursive((p[0], p[1] + 1), 1 + steps_so_far)
        else:
            right = float('inf')
        if 0 <= p[0] - 1 < rows and 0 <= p[1] < cols and matrix[p[0] - 1][
                p[1]] == False:
            up = recursive((p[0] - 1, p[1]), 1 + steps_so_far)
        else:
            up = float('inf')
        if 0 <= p[0] + 1 < rows and 0 <= p[1] < cols and matrix[p[0] + 1][
                p[1]] == False:
            down = recursive((p[0] + 1, p[1]), 1 + steps_so_far)
        else:
            down = float('inf')
        min_val = min(up, down, left, right)
        matrix[p[0]][p[1]] = False
        return min_val

    steps = recursive(start, 0)
    return steps if steps < float('inf') else None


# This is a BFS problem
from collections import deque


def bfs_min_steps(matrix, start, end):
    rows = len(matrix)
    if not rows:
        return 0
    cols = len(matrix[0])
    if not cols:
        return 0
    q = deque()
    q.append((start, 0))
    seen = set()
    while q:
        pos, steps = q.popleft()
        seen.add(pos)
        if pos == end:
            return steps
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= pos[0] + i < rows and 0 <= pos[1] + j < cols and matrix[
                    pos[0] + i][pos[1] + j] == False and (
                        pos[0] + i, pos[1] + j) not in seen:
                q.append(((pos[0] + i, pos[1] + j), steps + 1))

    return None
