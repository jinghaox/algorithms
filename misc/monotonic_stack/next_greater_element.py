def next_greater_element(nums):
    # 和daily temperature的基本一样
    # 区别是：第一次扫描时，不用计算和下一个更大值的距离，而是当前的值就是下一个最大值，直接将其放到res[poped_i]中
    # 在第一遍扫描之后，stack中还有剩余的值，再次从头扫描，但是这次不用再往stack加入新的数值了

    stack = []
    res = [-1]*len(nums)
    for i, val in enumerate(nums):
        while stack and val > stack[-1][0]:
            poped_val, poped_i = stack.pop()
            res[poped_i] = nums[i]
        stack.append([val, i])

    for i, val in enumerate(nums):
        while stack and val > stack[-1][0]:
            poped_val, poped_i = stack.pop()
            res[poped_i] = nums[i]
    
    return res

nums = [73,74,75,71,69,72,76,73]
ret = next_greater_element(nums)
print(ret)
