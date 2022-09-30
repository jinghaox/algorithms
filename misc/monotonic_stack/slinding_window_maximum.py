from queue import deque

def sliding_window_maximum_wrong(nums, k):
        # this is wrong for nums with some desceding elements

    res = []
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] > stack[-1]:
            stack.pop()
        stack.append(nums[i])
        if i>=k and stack[0] == nums[i-k]:
            stack.pop(0)
        if i >= k-1: 
            res.append(stack[0])
    return res 

def sliding_window_maximum(nums, k):
    q = [] # or using deque() # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.pop(0)
        # if window has k elements add to results 
        # (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res

def sliding_window_maximum_nested_loop(arr, k):
    res = []
    for i in range(len(arr)-2):
        c_max = max(arr[i:i+3])
        res.append(c_max)
    return res

def sliding_window_sum_sliding(nums, k):
    # [1,2,3,4,5,]
    # [1,2,3]
    # 对sliding window sum来讲，我们可以简单地加或是减一个数    
    # [1,2,3] - [1] + [4] = [2,3,4]
    # [2,3,4] - [2] + [5] = [3,4,5]
    # 但是对max来讲，怎么办？
    res = []
    n = len(nums)
    sliding_window_sum = sum(nums[:k])
    res.append(sliding_window_sum)
    # i 可以从0开始，但是实际上计算出来是的从1开始的sliding_window_sum
    for i in range(0, n-k):
        sliding_window_sum = sliding_window_sum - nums[i] + nums[i+k]
        res.append(sliding_window_sum)
    return res

def sliding_window_max_sliding(nums, k):
    # 但是对max来讲，怎么办？
    # 没想到好的办法，除非用monotonic stack
    # res = []
    # n = len(nums)
    # sliding_window_content = nums[:k]
    # curr_max = max(sliding_window_content)
    # res.append(curr_max)
    # for i in range(1, n-k+1):
    #     sliding_window_content.pop(0)
    #     curr_max = max(nums[i+k-1], curr_max)
    #     res.append(curr_max)
    # return res
    pass

arr = [1,3,2,5,4,3,1,8,7]
# arr = [4,3,2,1,0]
# arr = [1,3,1,2,0,5]
k = 3
ret = sliding_window_maximum_wrong(arr, k)
print(ret)
ret = sliding_window_maximum(arr, k)
print(ret)

# nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 3
# ret = sliding_window_sum_sliding(nums, k)
# ret = sliding_window_max_sliding(nums, k)
# print(ret)
