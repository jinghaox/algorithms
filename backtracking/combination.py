def combination(letters, k):
    def dfs_1(path, index, res, d):
        # d is the depth
        if d == k:
            res.append(path[:])
        if d> k:
            return
        for i in range(index, len(letters)):  # not using enumerate
            d = d+1
            path.append(letters[i])
            dfs_1(path, i+1, res, d)  ## here's the problem, using dfs(i+1), not dfs(index+1)
            path.pop()
            d = d-1
    
    def dfs(path, index, res):
        # actually we don't need depth d, we can use len(path) to decide when to stop
        # d is the depth
        if len(path) == k:
            res.append(path[:])
        for i in range(index, len(letters)):  # not using enumerate
            path.append(letters[i])
            dfs(path, i+1, res)  ## here's the problem, using dfs(i+1), not dfs(index+1)
            path.pop()

    res = []
    # dfs_1([], 0, res, 0)
    dfs([], 0, res)
    return res

ret = combination([1,2,3,4], 2)
print(ret)