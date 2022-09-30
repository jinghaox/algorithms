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

ret = generate_parenthesis(3)
print(ret)


        
