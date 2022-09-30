from typing import List

def count_smaller(nums: List[int]) -> List[int]:
    smaller_arr = [0] * len(nums)
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        l, r = 0, 0
        while l < len(left) or r < len(right):
            if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                # r>= len(right) means we have checked all elements in right array, 
                # so we only need to check left array next
                # or l < len(left) and left[l][1] <= right[r][1], 
                # means left array still has element and it's value is < the first element in right
                result.append(left[l])

                # here's the extra step, others are the same for merge sort 
                smaller_arr[left[l][0]] += r
                l += 1
            else:
                result.append(right[r])
                r += 1
        return result

    ret = merge_sort(list(enumerate(nums)))
    # return ret
    return smaller_arr

nums = [3,6,7,1,5,8,2,4]
ret = count_smaller(nums)
print(ret)