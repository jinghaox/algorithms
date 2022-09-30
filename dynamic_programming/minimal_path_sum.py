from math import inf
def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[inf for _ in range(rows)] for _ in range(cols)]

    dp[0][0] = grid[0][0]
    for r in range(1, rows):
        dp[r][0] = dp[r-1][0] + grid[r][0]

    for c in range(1, cols):
        dp[0][c] = dp[0][c-1] + grid[0][c] 
    
    print(dp)

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    print(dp)
    
    return dp[-1][-1]

grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

ret = min_path_sum(grid)
print(ret)
    