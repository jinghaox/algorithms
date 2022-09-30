from collections import deque
def longestSubarray_intuitive(nums, limit):
    max_len = 0
    for i in range(len(nums)):
        max_num, min_num = nums[i], nums[i]
        for j in range(i+1, len(nums)):
            max_num = max(max_num, nums[j])
            min_num = min(min_num, nums[j])
            if max_num - min_num <= limit:
                max_len = max(max_len, j-i+1)
    return max_len

def longestSubarray_intuitive_improved(nums, limit):
    # set i as right boundary
    # find left boundary
    max_len = 0
    for i in range(len(nums)):
        max_num, min_num = nums[i], nums[i]
        for j in range(i, -1, -1):
            max_num = max(max_num, nums[j])
            min_num = min(min_num, nums[j])
            if max_num - min_num <= limit:
                max_len = max(max_len, i-j+1)
    return max_len

def longestSubarray(nums, limit):
    # use two queues
    min_queue = deque()
    max_queue = deque()

    max_len = 0
    i = 0
    j = 0
    # for j in range(len(nums)):
    while j < len(nums):
        # min_queue is a monotonic queue, the first number is the smallest number between i&j
        # the 2nd is the 2nd smallest number between i&j
        while min_queue and min_queue[-1] > nums[j]:
            min_queue.pop()
        min_queue.append(nums[j])

        while max_queue and max_queue[-1] < nums[j]:
            max_queue.pop()
        max_queue.append(nums[j])

        if max_queue[0] - min_queue[0] <= limit:
            max_len = max(max_len, j-i+1)
        else:
            if max_queue[0] == nums[i]:
                max_queue.popleft()
            if min_queue[0] == nums[i]:
                min_queue.popleft()
            
            i += 1
        j += 1
    return max_len

nums = [8,2,4,7]
limit = 4

# nums = [10,1,2,4,7,2]
# limit = 5
# 
# nums = [4,2,2,2,4,4,2,2]
# limit = 0

ret = longestSubarray(nums, limit)
print(ret)
