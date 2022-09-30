def longest_sub_len(nums):
    # for dp[i]
    # we need to compare all dp[j]+1 with it, where 0 <= j < i
    # if nums[j] < nums[i], then we don't update dp[i], but we can't set dp[i] to -inf either
    # because it can't be -inf
    # initialize all to 1, since a number by itself is of length 1
    # dp = [float('-inf')]* len(nums)
    # dp[0] = 2
    dp = [1]*len(nums)

    best = 0
    for i in range(len(nums)):
        for j in range(i): 
            if nums[j] < nums[i]:
                dp[i] = max(dp[j]+1, dp[i])
            # this is not correct
            # else:
            #     dp[i] = dp[i-1]
        best = max(best, dp[i])
    print(dp)
    
    return best

# nums = [1,2,4,3]
nums = [50, 3, 10, 7, 40, 80, 10,20,30]
ret = longest_sub_len(nums)
print(ret)