from collections import Counter
from typing import List

def subarray_sum_mine(arr, target):
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum.append(arr[i] + prefix_sum[i-1])
    print(prefix_sum)

    for right in range(len(arr)):
        complement = prefix_sum[right] - target
        if complement in prefix_sum:
            left = prefix_sum.index(complement) + 1
            return [left, right+1]
    return [-1, -1]

def subarray_sum(arr, target):
    # no need to loop twice
    prefix_sum = {0:0}  # this is necessary, since the subarr may start from index 0, and it has prefix_sum 0 
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sum:
            # why we shouldn't use prefix_sum[complement]+1 here, because for 0:0, we need to return 0
            # why append i+1 here, we append the rightmost (the next one to the correct index)
            # e.g. 3 1 2 5 1, we got prefix_sum
            #        1   3   5
            # so the subarray is actually [0:1], [1:3], [3:5]
            print(prefix_sum)
            return [prefix_sum[complement], i+1]
        else:
            print(prefix_sum)
            prefix_sum[cur_sum] = i + 1

def subarray_sum_total_mine(arr, target):
    # prefix_sum may have duplicate value
    # e.g. [10, 15, 10, -10, 0] 
    # now we can't use dictionary, since the same key's value will be updated
    # we can change it to [10:[0,3], 15:[1]]
    prefix_sum = {0:[0]} 
    cur_sum = 0
    res = []
    ans = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sum:
            for p in prefix_sum[complement]:
                res.append([p, i+1])
                print(arr[res[-1][0]:res[-1][1]])
                ans += 1
        if cur_sum in prefix_sum:
            prefix_sum[cur_sum].append(i + 1)
        else:
            prefix_sum[cur_sum] = [i + 1]
    return ans 

def subarray_sum_total(arr: List[int], target: int) -> int:
    prefix_sums = Counter()
    prefix_sums[0] = 1 # since empty array's sum is 0
    cur_sum = 0
    count = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            count += prefix_sums[complement]
        prefix_sums[cur_sum] += 1
    return count

def subarray_sum_divisible_mine(nums, k):
    # 3 1 2 5 1 divisible by 3
    # prefix_sum is 3 4 6 11 12
    # compl= %k     0 1 0 5 0   not finding %k == 0
    # but to count for each complement, before it, how many occurance happened
    # Initial counter    {0:1}
    # Then          0  count+=1, count=1, {0:2}
    #                 1                   {0:2, 1:1}
    #                   0 count+=2, count = 3, {0:3, 1:1}
    #                     5                    {0:3, 1:1, 5:1}
    #                       0, count+=3, count=3+3=6, {0:4, 1:1, 5:1}

    prefix_sum_remainder = {0: [0]}
    cur_sum = 0
    ans = 0

    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum%k in prefix_sum_remainder:
            prefix_sum_remainder[cur_sum%k].append(i) 
        else:
            prefix_sum_remainder[cur_sum%k] = [i+1]
    print(prefix_sum_remainder)
    res = []
    all_indecies = prefix_sum_remainder[0]
    print(all_indecies)
    while all_indecies:
        cur = all_indecies.pop(0)
        for x in all_indecies:
            res.append(nums[cur:x])
            ans += 1
    print(res)
    return ans

def subarray_sum_divisible(nums: List[int], k: int) -> int:
    remainders = Counter({0: 1})
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        cur_sum += num
        remainder = cur_sum % k
        # seems this line is not necessary, and this line is hard to understand
        # complement = (k - remainder) % k
        complement = remainder
        if complement in remainders:
            count += remainders[complement]
        remainders[complement] += 1

    return count
    

arr = [1,3,-3,8,5,7]
target = 5
ret = subarray_sum(arr, target)
print(ret)
# arr = [1, -20, -3, 30, 5, 4, 1, -3, 2]
# target = 7
# arr = [1, 1, 1]
# target = 3

# arr = [10, 5, -5, -20, 10]
# target = -10
# ret = subarray_sum_total_mine(arr, target)
# print(ret)

# arr = [4, 5, 0, -2, -3, 1] 
# target = 5 
# ret = subarray_sum_total(arr, target)
# print(ret)

# # # nums = [3,1,2,5,1]
# # # k = 3
# nums = [0, 37, 0, 7, 9, 4, 101]
# k = 18
# # nums = [4, 5, 0, -2, -3, 1] 
# # k = 5 
# ret = subarray_sum_divisible(nums, k)
# print(ret)


# # nums = [3,1,2,5,1]
# # k = 3
# nums = [0, 37, 0, 7, 9, 4, 101]
# k = 18
# ret = subarray_sum_divisible(nums, k)
# print(ret)
