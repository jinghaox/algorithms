def unique_paths(m,n):
    dp = [[0 for i in range(n)] for j in range(m)]

    # need to initialize first row and col
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

m = 2
n = 3
ret = unique_paths(m,n)
print(ret)