import pandas as pd
import numpy as np
from collections import deque

map_design = np.array([
    [  2,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [  0,  3,  0,  4,  0,  5,  0,  6,  0,  0],
    [  0,  0,  0,  0,  7,  0,  0,  8,  0,  0],
    [  0,  9,  0, 10,  0, 11,  0, 12,  0,  0],
    [  0,  0,  0,  0, 13,  0,  0,  0, 14,  0],
    [  0, 15,  0, 16,  0, 17,  0, 18,  0,  0],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
])

map_df = pd.DataFrame(map_design)

ed_x = map_df.shape[0]
en_y = map_df.shape[1]

def start_position(map, start, end):
    max_x = map.shape[0]
    max_y = map.shape[1]

    for i in range(max_x):
        for j in range(max_y):
            if map[i][j] == start:
                st_x, st_y = i, j
            if map[i][j] == end:
                ed_x, ed_y = i+1, j+1
    return bfs(map, st_x, st_y, ed_x, ed_y)


def bfs(map_design, st_x, st_y, ed_x, en_y):
    q = deque()
    visited = np.array([[1] * en_y for _ in range(ed_x)])
    q.append((st_x, st_y))

    while True:
        if len(q) == 0:
            break
        direction = [(1,0), (-1,0), (0, 1), (0, -1)]
        current_x, current_y = q.popleft()
        for x, y in direction:
            next_x = current_x + x
            next_y = current_y + y

            if next_x < 0 or next_y < 0 or next_x >= ed_x or next_y >= en_y:
                continue
            if map_design[current_x][current_y] >= 3:
                break
            if visited[next_x][next_y] == 1:
                q.append([next_x, next_y])
                visited[next_x][next_y] = visited[current_x][current_y] + 1

    if visited[ed_x - 1][en_y - 1] == 1:
        return -1
    else :
        return visited[ed_x - 1][en_y -1]

print(start_position(map_design, 2, 10))