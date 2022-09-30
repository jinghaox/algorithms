def subsets(nums):
    res = []
    path = []
    def dfs(i):
        if i == len(nums):
            res.append(path[:])
            return 

        # nums[i] is included 
        path.append(nums[i])
        dfs(i+1)

        # nums[i] is NOT included 
        path.pop()
        dfs(i+1)

        # # another way is, this will output in reverse order
        # # first not include nums[i]
        # dfs(i+1)
        # # then add nums[i]
        # path.append(nums[i])
        # dfs(i+1)
        # # then backtrack
        # path.pop()
    
    dfs(0)
    return res

nums = [1,2,3]
ret = subsets(nums)
print(ret)