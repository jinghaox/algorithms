from typing import List

def can_partition(nums: List[int]) -> bool:
    # dfs with memoiazation
    # target must be sum/2
    target = sum(nums)/2

    # dfs
    used = [False]*len(nums)
    def dfs(cur_sum):
        # return True or False
        if cur_sum == target:
            return True 
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            if dfs(cur_sum + nums[i]):
                return True
            used[i] = False
        return False
    
    return  dfs(0)

def can_partition_dp(nums: List[int]) -> bool:
    if len(nums) < 2: return False
    nums_sum = sum(nums)
    if nums_sum % 2 == 1: return False
    nums_sum //= 2
    dp = [False] * (nums_sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(nums_sum, num - 1, -1):
            print(f"i = {i}, i-num = {i-num}")
            dp[i] = dp[i] or dp[i - num]
    return dp[nums_sum]

nums = [1,5,11,5]
# nums = [1,6,6, 11]
ret = can_partition_dp(nums)
print(ret)


