def palindrome_partition(s):

    def is_palindrom(st):
        return st == st[::-1]

    n = len(s)
    res = []
    def dfs(start_index, path, res):
        if start_index == n:
            res.append(path[:])
            return
        # starting at start_index+1, since current index is start_index, 
        # and we want to check start_index:start_index+1, start_index+2, start_index+3,...
        for i in range(start_index+1, n+1):
            if is_palindrom(s[start_index:i]):
                path.append(s[start_index:i])
                dfs(i, path, res)
                path.pop()
    
    dfs(0, [], res)
    return res

s = "aabb"
ret = palindrome_partition(s)
print(ret)
