def three_sum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        new_target = target - nums[i]
        left = i+1
        right = len(nums)-1
        if i > 0 and nums[i] == nums[i-1]:
            # because i-1 means i >= 1
            continue
        while left < right:
            if nums[left] + nums[right] < new_target:
                left += 1
            elif nums[left] + nums[right] > new_target:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                # can only update left, not right
                # no need to shift right pointer, since it can be checked by if > new_target
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
target = 0
ret = three_sum(nums, target)
print(ret)
