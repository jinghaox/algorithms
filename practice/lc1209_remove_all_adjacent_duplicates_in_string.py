def remove_duplicates(s, k):
    stack = []
    for i in range(0, len(s)):
        # if not stack:
        #     stack.append([s[i], 1])
        # elif stack[-1][0] == s[i] and stack[-1][1] == k-1:
        #     stack.pop()
        # elif stack[-1][0] == s[i] and stack[-1][1] < k-1:
        #     stack[-1][1] += 1
        # else:
        #     stack.append([s[i], 1])
        if stack and stack[-1][0] == s[i]:
            stack[-1][1] += 1
        else:
            stack.append([s[i], 1])
        if stack[-1][1] == k:
            stack.pop()
    
    res = ''
    for c, i in stack:
        res  += c*i

    return res 


s = "inntttuuuiitttivve"
k = 3
ret = remove_duplicates(s, k)
print(ret)

