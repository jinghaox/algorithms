from typing import List

def find_largest_subset(nums: List[int]) -> int:
    # when i =4, max_subsets = 1, 2, 3, 1
    nums.sort()
    max_subsets = []
    for i, num in enumerate(nums):
        if i == 3:
            i=3
        max_num_of_subsets= 0
        for j in range(i):
            if num % nums[j] == 0:
                max_num_of_subsets = max(max_num_of_subsets, max_subsets[j])
        max_subsets.append(max_num_of_subsets + 1)
    return max(max_subsets)

nums = [2,4,8,11,88]
ret = find_largest_subset(nums)
print(ret)