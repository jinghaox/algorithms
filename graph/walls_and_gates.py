from collections import deque
from doctest import DebugRunner
from smtpd import DebuggingServer
from typing import List

delta_row = [0, 1, 0, -1]
delta_col = [1, 0, -1, 0]

INF = 2**31

def map_gate_distances(dungeon_map):
    q = deque()
    num_rows, num_cols = len(dungeon_map), len(dungeon_map[0])

    # same as below, but different implementations
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                q.append((i, j))
    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         if dungeon_map[i][j] == 0:
    #             q.append((i, j))

    while q:
        print(q)
        r, c = q.popleft()
        for i in range(len(delta_row)):
            n_r = r + delta_row[i]
            n_c = c + delta_col[i]
            if 0 <= n_r < num_rows and 0 <= n_c < num_cols:
                if dungeon_map[n_r][n_c] == INF:
                    dungeon_map[n_r][n_c] = dungeon_map[r][c] + 1
                    q.append((n_r, n_c))
    return dungeon_map

dungeon_map = [
  [INF, -1, 0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0, -1, INF, INF],
]

ret = map_gate_distances(dungeon_map)
print(ret)
