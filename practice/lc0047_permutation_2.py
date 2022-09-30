def permutation_2(nums):
    counter = {i:0 for i in nums}
    for i in nums:
        counter[i] += 1
    path = []
    res = []
    def dfs():
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in counter:
            if counter[i] != 0: # or > 0
                path.append(i)
                counter[i] -= 1
                dfs()
                path.pop()
                counter[i] += 1
        
    dfs()
    return res

def permutation(nums):
    path = []
    res = []
    used = [False]*len(nums)
    def dfs():
        if len(path) == len(nums):
            res.append(''.join(path[:]))
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return res


# nums = [1,1,2]
nums = 'abc'
ret = permutation(nums)
print(ret)