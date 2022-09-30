# [1,2,5] amount = 11
# output is [5,5,1], fewest number of coins
# [1,3,4,5] amount = 7
# can't use greedy algorithm, since 5+1+1 (3) > 3+4 (2)

def coin_change_dfs(nums, target):
    def dfs(path, target, res, min_len):
        if target == 0:
            # we can shrink the res by checking the length of path
            if min_len[0] > len(path):
                min_len[0] = len(path)
                res.append(path[:])
            return
        if target < 0:
            return
        for x in nums:
            # we can check x<=target here, or use if target<0 in above
            # if x <= target:
            path.append(x)
            dfs(path, target-x, res, min_len)
            path.pop()
        
    res = []
    min_len = [float('inf')]
    dfs([], target, res, min_len)
    return res

def coin_change_dfs_memo(nums, target):
    # not working yet
    def dfs(path, target, res, memo):
        if target in memo: 
            return memo[target]
        if target == 0:
            res.append(path[:])
            return target 
        if target < 0:
            return target
        val = -1 
        for x in nums:
            path.append(x)
            ret = dfs(path, target-x, res, memo)
            if ret == 0:
                val = x 
                path.pop()
                memo[target] = val 
            else:
                path.pop()
        return val 
        
    res = []
    memo = {}
    dfs([], target, res, memo)
    print(memo)
    return res

def coin_change_dp(nums, target):
    # bottom up, starting from dp[1]
    dp = [float('inf')]*(target+1)
    # need dp[0] to be 0, since dp[target-coin] = dp[1-1] = dp[0], should be 0
    # means for target 0, we will need 0 coins
    dp[0] = 0

    for i in range(1, target+1):
        for c in nums:
            if c <= i:
                dp[i] = min(1+ dp[i-c], dp[i])
    # return dp[-1]
    return dp[target] if dp[target] != float('inf') else -1

nums = [1,3,4,5]
target = 7
ret = coin_change_dfs_memo(nums, target)
print(ret)

# nums = [1,3,5]
# target = 11 
# nums = [3,5,6]
# target = 7 
# ret = coin_change_dp(nums, target)
# print(ret)

