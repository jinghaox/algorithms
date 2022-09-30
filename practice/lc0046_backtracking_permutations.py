def bt_permutations(nums):
    res = []
    used = {x:False for x in nums}
    path = []

    def dfs(res, used, path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for x in nums:
            if used[x]:
                continue
            used[x] = True
            path.append(x)
            dfs(res, used, path)
            path.pop()
            used[x] = False
    dfs(res, used, path)
    return res

def permutations_without_dfs(nums):    
    # 1, 2, 3 
    # first remove 1 -> 2, 3
    # then  remove 2, -> 3
    # then  return 3, add 2 back -> 3, 2
    # then  remove 3, -> 2
    # then  return 2, add 3 back -> 2, 3
    # now we have [3,2], [2,3]
    # then append 1 back
    # -> 3, 2, 1
    # -> 2, 3, 1

    # this is hard to understand，因为pop(0)（从左边pop），再append（从右边append）
    # 这个是去掉1的
    # [4, 3, 2, 1], 
    # [3, 4, 2, 1], 
    # [2, 4, 3, 1], 
    # [4, 2, 3, 1], 
    # [3, 2, 4, 1], 
    # [2, 3, 4, 1], 
    # 这个是去掉2的，看第一个，倒过来是2，3，4，即2，3，4还没有做，故下一步是去掉2
    # [1, 4, 3, 2], 
    # [4, 1, 3, 2], 
    # [3, 1, 4, 2], 
    # [1, 3, 4, 2], 
    # [4, 3, 1, 2], 
    # [3, 4, 1, 2], 
    # 这个是去掉3的，看第一个，倒过来是3，4，即还剩下3，4没有做，故下一步是去掉3
    # [2, 1, 4, 3], 
    # [1, 2, 4, 3], 
    # [4, 2, 1, 3], 
    # [2, 4, 1, 3], 
    # [1, 4, 2, 3], 
    # [4, 1, 2, 3], 
    # 这个是去掉4的，看第一个，倒过来是4
    # [3, 2, 1, 4], 
    # [2, 3, 1, 4], 
    # [1, 3, 2, 4], 
    # [3, 1, 2, 4], 
    # [2, 1, 3, 4], 
    # [1, 2, 3, 4]

    res = []
    # here's the base case
    if (len(nums)) == 1:
        return [nums[:]]
    
    # this is the same as below
    # for x in nums:
    #     nums.pop(0)
    for i in range(len(nums)):
        x = nums.pop(0)

        perms = permutations_without_dfs(nums)
        # it will have multiple perms returned, [3,2], [2,3]
        for p in perms:
            p.append(x)
        res.extend(perms)
        # backtrack
        # do NOT insert to front, as 3 -> 2,3 -> 3 -> 2,3 again
        # nums.insert(0, x)
        # here's backtracking, but not to the original place
        nums.append(x)
    return res

nums = [1,2,3,4]
# ret = bt_permutations(nums)
ret = permutations_without_dfs(nums)
print(ret)