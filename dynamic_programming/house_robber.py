# leetcode 198
from typing import List
def rob(nums: List[int]) -> int:
    # this one uses O(N) space, we can use just 2 elements, i.e. dp[i-1] and dp[i-2]
    # see below
    dp = [0]*len(nums)
    dp[0] = nums[0]
    # here must be max, since dp[1] can be dp[0] if nums[1] is < nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    
    return dp[-1]

def rob_new(nums):
    # rob1, rob2, nums[i], nums[i+1]
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(rob1+n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

nums = [2,7,9,3,1]
ret = rob_new(nums)
print(ret)
