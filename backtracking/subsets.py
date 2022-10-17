def sub_sets(nums):
    def dfs(index, path, res):
        if index == len(nums):
            return

        # why do we append here?
        print(f"for {nums[index]}")
        res.append(path + [nums[index]])
        print(res)

        # recursion call including nums[index]
        path.append(nums[index])
        dfs(index+1, path, res)
        path.pop()

        # by here, we have
        # [[], [1]]
        # [[], [1], [1, 2]]
        # [[], [1], [1, 2], [1, 2, 3]]

        # recursion call without nums[index]
        dfs(index+1, path, res)

        # 为什么是[[]]? 因为需要[]
    res = [[]]
    dfs(0, [], res)
    return(res)

nums = [1,2,3]
ret = sub_sets(nums)
print(ret)