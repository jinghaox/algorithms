def combination_sum_with_dup(nums, target):
    # this will have duplicate results, such as [2,2,3], and [2,3,2]
    # the solution is, only go forward, not backward, if 2 has been used, then don't go back and use it again
    # so for x in nums won't work, we need to use index, and only use numbers after the current index
    # so code below
    res = []
    path =[]
    def dfs(path, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        
        for x in nums:
            path.append(x)
            dfs(path, remaining-x)
            path.pop()
    
    dfs([], target)
    return res

def combination_sum(nums, target):
    # this will have duplicate results, such as [2,2,3], and [2,3,2]
    # the solution is, only go forward, not backward, if 2 has been used, then don't go back and use it again
    # so for x in nums won't work, we need to use index, and only use numbers after the current index
    # so code below
    res = []
    path =[]
    def dfs(index, path, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        
        for i, x in enumerate(nums):
            if i < index:
                continue
            path.append(x)
            dfs(i, path, remaining-x)
            path.pop()

            # the above can be simplified to
            # for i in range(index, len(nums)):
            #     path.append(nums[i])
            #     dfs(i, path, remaining - nums[i])
            #     path.pop()
    
    dfs(0, [], target)
    return res

def combination_sum_alternative(nums, target):
    # this will have duplicate results, such as [2,2,3], and [2,3,2]
    # the solution is, only go forward, not backward, if 2 has been used, then don't go back and use it again
    # so for x in nums won't work, we need to use index, and only use numbers after the current index
    # so code below
    res = []
    path =[]
    def dfs(index, path, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        if index >= len(nums) or remaining < 0:
            return
        # include nums[index]        
        path.append(nums[index])
        dfs(index, path, remaining-nums[index])
        path.pop()
        # not include nums[index], just use next char @ index+1
        dfs(index+1, path, remaining)
    
    dfs(0, [], target)
    return res

def combination_sum2(candidates, target):
    def dfs(index, path, res, remaining):
        # shall I return 0 or return? 
        # no need to return 0, since remaining tells us what is remained for each dfs call
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            # if remaining < 0, then this res is not valid, will be discarded
            # later on, after this return, path will pop, 
                      # so all numbers in path will be discarded
            # algomonster did remaining-num check inside the for loop
            return
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            # if remaining - candidates[i] < 0:
            #     continue
            dfs(i, path, res, remaining-candidates[i])
            # here is dfs(i), 
            path.pop()
    res = [] 
    dfs(0, [], res, target)
    return res

ret = combination_sum_alternative([2,3,6,7], 7)
print(ret)

