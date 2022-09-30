def daily_temperatures_tricky(t):
    # 这个很tricky，但是work，见one notes
    res = [0] * len(t)
    stack = [] #stores[temp, index]
    for i, temp in enumerate(t):
        while stack and stack[-1][0] < temp:
            _, poped_i = stack.pop()
            res[poped_i] = (i - poped_i)
        stack.append((temp, i))
    
    return res

def daily_temperatures(t):
    # Stores a decreasing list of temperature by index
    # 它的算法是，反过来算
    # 如果当前的值比stack中的大，就把stack中的值pop出来
    # 如果当前值小，就把它加到stack的最后，这样，stack最后一个值是比当前值大的最近的值
    # 其差就是相距的天数
    stack = []
    ans = []
    n = len(t)
    # For this implementation, we start from the reverse
    for i in reversed(range(n)):
        element = t[i]
        # Special case when `i == n - 1`, which is the last day
        if i == n - 1:
            stack.append(i)
            ans.append(0)
            continue
        while stack and element >= t[stack[-1]]:
            stack.pop()
        # If `stack` is nonempty, there is a next big temperature, so we store it
        # in `ans`. Otherwise, there are no bigger temperature, so we record `0`
        if stack:
            ans.append(stack[-1] - i)
        else:
            ans.append(0)
        stack.append(i)
    # The answer is appended in reverse order, so we need to reverse the list first
    return reversed(ans)

t = [73,74,75,71,69,72,76,73]
ret = daily_temperatures(t)
print(ret)
        
