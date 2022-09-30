def sub_sets(nums):
    def dfs(index, path, res):
        if index == len(nums):
            return

        res.append(path + [nums[index]])

        # recursion call including nums[index]
        path.append(nums[index])
        dfs(index+1, path, res)
        path.pop()

        # recursion call without nums[index]
        dfs(index+1, path, res)

        # 为什么是[[]]? 因为需要[]
    res = [[]]
    dfs(0, [], res)
    return(res)

nums = [1,2,3]
ret = sub_sets(nums)
print(ret)