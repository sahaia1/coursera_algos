# Complete the function below.
import sys
import os
from collections import deque

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_neighbours(pos, rows, cols):
    neighbours = []
    for dr, dc in directions:
        new_row = pos[0] + dr
        new_col = pos[1] + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbours.append((new_row, new_col))
    return neighbours


def get_rows_cols(grid):
    return len(grid), len(grid[0])


def get_start_and_end(grid, nr, nc):
    start, end = None, None
    for i in range(nr):
        for j in range(nc):
            if not start or not end:
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] == '+':
                    end = (i, j)
            else:
                break
    return start, end


def is_key(pos, grid):
    return ord('a') <= ord(grid[pos[0]][pos[1]]) <= ord('z')


def is_door(pos, grid):
    return ord('A') <= ord(grid[pos[0]][pos[1]]) <= ord('Z')


def is_water(pos, grid):
    return grid[pos[0]][pos[1]] == '#'


def find_shortest_path(grid):
    targets = []
    path = []

    num_rows, num_cols = get_rows_cols(grid)

    _, end = get_start_and_end(grid, num_rows, num_cols)

    queue = deque()

    queue.append((end, []))
    targets.append(['@', set()])
    target_set = set('@')
    while queue:
        pos, path_so_far = queue.popleft()
        print(pos, grid[pos[0]][pos[1]], targets[-1][0], targets[-1][1])
        if pos not in targets[-1][1]:
            targets[-1][1].add(pos)
            if grid[pos[0]][pos[1]] == targets[-1][0]:
                _, s = targets.pop()
                # Empty Queue
                queue = deque()
                if not targets:
                    path = path_so_far + [pos]
                    break
                else:
                    targets[-1][1] = targets[-1][1] - s
            if is_door(pos, grid):
                if grid[pos[0]][pos[1]].lower() not in target_set:
                    s = set()
                    s.add(pos)
                    targets.append([grid[pos[0]][pos[1]].lower(), s])
                    target_set.add(grid[pos[0]][pos[1]].lower())
            for neighbour in get_neighbours(pos, num_rows, num_cols):
                if neighbour not in targets[-1][1] and not is_water(
                        neighbour, grid):
                    queue.append((neighbour, path_so_far + [pos]))

    return path[::-1]


if __name__ == "__main__":
    f = sys.stdout

    grid_cnt = 0
    grid_cnt = int(input())
    grid_i = 0
    grid = []
    while grid_i < grid_cnt:
        try:
            grid_item = str(input())
        except:
            grid_item = None
        grid.append(grid_item)
        grid_i += 1

    res = find_shortest_path(grid)
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")

    f.close()