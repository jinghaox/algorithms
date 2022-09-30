def generate_parenthese(n):
    def dfs(start_index, res, left_count, right_count, path):
        if start_index == n*2:
            res.append(''.join(path))
            return
        
        for pa in ['(', ')']:
            if pa == '(' and left_count >= n:
                continue
            if pa == ')' and right_count >= left_count:
                continue
            path.append(pa)
            if pa == '(':
                left_count += 1
            else:
                right_count += 1
            dfs(start_index+1, res, left_count, right_count, path)
            # below is backtracking
            if pa == '(':
                left_count -= 1
            else:
                right_count -= 1
            path.pop()
    
    # res = []
    # dfs(0, res, 0, 0, [])
    # return res

    def dfs2(start_index, res, left_count, right_count, path):
        if start_index == n*2:
            res.append(''.join(path))
            return
        if left_count < n:
            path.append('(')
            dfs2(start_index+1, res, left_count+1, right_count, path)
            path.pop()

        # do NOT use elif here, since after we append '(', we may still want to append')'
        if right_count < left_count:
            path.append(')')
            dfs2(start_index+1, res, left_count, right_count+1, path)
            path.pop()

    res = []
    dfs2(0, res, 0, 0, [])
    return res

n = 3
ret = generate_parenthese(n)
print(ret)