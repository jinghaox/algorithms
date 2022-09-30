def max_product(nums):
    res = max(nums)
    cur_max, cur_min = 1, 1
    for n in nums:
        # no need to check if n == 0 or not
        temp1 = cur_max * n
        temp2 = cur_min * n

        cur_max = max(temp1, temp2, n)
        cur_min = min(temp1, temp2, n)
        res = max(res, cur_max)
    return res

nums = [-2.5, 4, 0, 3, 0.5, -8, -3, -9]
ret = max_product(nums)
print(ret)