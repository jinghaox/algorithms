from typing import List
def maximal_square(matrix: List[List[int]]) -> int:
    # if matrix[r][c]==1, dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
    # ow, matrix[r][c]==0, dp[r][c] = 0 (can't make a square here)
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    best = 0  # keep track of the largest square side size as we go

    # fill top row
    for r in range(m):
        dp[r][0] = matrix[r][0]
        # don't forget to get best here
        best = max(dp[r][0], best)

    # fill leftmost column
    for c in range(n):
        dp[0][c] = matrix[0][c]
        best = max(dp[0][c], best)

    # fill internal cells
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:  # skip 0 cells
                continue
            # recurrence relation, see above explanation
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
            best = max(best, dp[r][c])
    
    print(dp)

    return best * best

def maximal_square_mine(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    
    dp = [row[:] for row in matrix]  # make a deep copy of 2d array
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = 0
    
    max_r = max(dp[0][:]) 
    max_c = max(dp[:][0])
    max_s = max(max_r, max_c)

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                continue
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                max_s = max(max_s, dp[i][j])

    return max_s**2

# matrix = [[1, 1, 1],
#           [1, 1, 1],
#           [0, 1, 0]]

# matrix = [[1, 0, 1, 0, 0],
#           [1, 0, 1, 1, 1],
#           [1, 1, 1, 1, 0],
#           [1, 0, 0, 1, 0]]

matrix = [[0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 1, 0]]
ret = maximal_square_mine(matrix)
print(ret)