from typing import List

def plumber(grid: List[List[int]]) -> int:
    # append -1 to the last column, 
    # so it can be used to terminate the check for each row
    for row in grid:
        row.append(-1)

    prev = []

    start = 0
    coins = 0
    for i, val in enumerate(grid[0]):
        # first get the prev for the first row
        # for [1,0,-1,  1,0,1]
        # out put will be
        #     [1,1,-inf,2,2,2]
        if val == 0:
            pass
        elif val == 1:
            coins += 1
        elif val == -1:
            for j in range(start, i):
                prev.append(coins)
            prev.append(float('-inf'))
            start = i + 1
            coins = 0

    for level in range(1, len(grid)):
        cur = []
        row = grid[level]
        prev_max = float('-inf')
        start = 0
        coins = 0
        for i, val in enumerate(row):
            if val == 0:
                prev_max = max(prev_max, prev[i])
            elif val == 1:
                prev_max = max(prev_max, prev[i])
                coins += 1
            elif val == -1:
                for j in range(start, i):
                    cur.append(prev_max + coins)
                cur.append(float('-inf'))
                start = i + 1
                coins = 0
                prev_max = float('-inf')
        prev = cur

    cur_max = max(cur)
    if cur_max < 0:
        return -1
    return cur_max

grid = [[1, 0,-1, 1,0, 1],
        [1,-1, 1,-1,1,-1],
        [0, 0,-1,-1,1, 1]]
ret = plumber(grid)
print(ret)