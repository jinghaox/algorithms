def generate_parenthesis(n):
    res = []
    path = []
    def backtrack(open_p, closed_p):
        if open_p == closed_p == n:
            res.append("".join(path))
            return 
        # if we swap the order of the two blocks below, we will get the same results but in different order
        if open_p < n:
            path.append("(")
            backtrack(open_p+1, closed_p)
            path.pop()
        if closed_p < open_p:
            path.append(")")
            backtrack(open_p, closed_p+1)
            path.pop()
    
    backtrack(0,0)
    return res

def generate_parenthesis_mock(n):
    res = []
    path = []
    def backtrack(i, left_count, right_count):
        if i == n*2:  # here it should be n*2, and we actually don't need this extra arg i, see above
            res.append(''.join(path[:]))
            return
        if left_count < n:
            path.append('(')
            backtrack((i+1), left_count+1, right_count)
            path.pop()
        if left_count > right_count:
            path.append(')')
            backtrack((i+1), left_count, right_count+1)
            path.pop()
    backtrack(0, 0, 0)
    return res
        
ret = generate_parenthesis_mock(3)
print(ret)


        
