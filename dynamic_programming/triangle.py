from functools import lru_cache
from math import inf
from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)

    @lru_cache(None)
    # lru_cache is used for memoization
    def dfs(i, level):
        if level == n:
            return 0

        best = inf
        next_level = level + 1
        for nexti in [i, i + 1]:
            # print(f"nexti = {nexti}, next_level = {next_level}")
            best = min(best, dfs(nexti, next_level))
            # why do we need this 0<= nexti <=next_level?
            # if 0 <= nexti <= next_level:
            #     best = min(best, dfs(nexti, next_level))
        ret = best + triangle[level][i]
        print(f"level = {level}, ret = {ret}, {triangle[level][i]}")
        return ret

    return dfs(0, 0)

def minimum_total_dp(triangle: List[List[int]]) -> int:
    # init dp array as the last row of the triangle
    # dp = [triangle[-1][c] for c in range(len(triangle[-1]))]    
    dp = triangle[-1][:]

    for r in range(len(triangle)-2, -1, -1):
        for c in range(r+1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c+1])
    print(dp)
    return dp[0]

def minimum_total_dfs(triangle):
    memo = {} 
    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        if r == len(triangle) - 1: 
            # reaches the last line
            return triangle[r][c]
        memo[(r, c)] = triangle[r][c] + min(dfs(r+1, c), dfs(r+1, c+1))
        # current triangle element + min (next level at c's dfs return, next level at c+1's dfs return)
        return memo[(r,c)]
    return dfs(0, 0)


triangle = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3],
    [10,11,12,9,1]
]
# ret = minimum_total_dp(triangle)
ret = minimum_total_dfs(triangle)
print(ret)