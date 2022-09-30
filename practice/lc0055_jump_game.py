def jump_game_dp(nums):
    dp = [False]*len(nums)
    dp[-1] = True
    for i in range(len(nums)-2, -1, -1):
        if nums[i] == 0:
            dp[i] = False
        else:
            for j in range(i+1, i+nums[i]+1):
                if dp[j] == True:
                    dp[i] = True
                    break
            if j == i+nums[i]+1:
                dp[i] = False
    print(dp)
    return dp[0]

def jump_game_greedy(nums):
    # goal is the index that we can reach, first initialized to the last element
    goal = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        # note: here should be >=, not just >
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


# nums = [2,3,1,0,4]
nums = [3,2,1,0,4]
# ret = jump_game_dp(nums)
ret = jump_game_greedy(nums)
print(ret)
