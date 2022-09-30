def longest_repeating_char(s, k):
    left = 0
    n = len(s)
    counts = {}
    res = 0 
    for right in range(n):
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_cnt = max(counts.values())
        print(s[left:right+1])
        while right-left+1 - max_cnt > k:  # here we can use while, or if, although it's different, the result is the same
            counts[s[left]] -= 1
            left += 1
        # here, left is changed, so right-left+1 is actually change,
        # so we can't save right-left+1 before, and use it here,
        # we have to update it here
        res = max(res, right-left+1)
    return res

def longest_repeating_char_better(s, k):
    left = 0
    n = len(s)
    maxf = 0
    res = 0 
    counts = {}
    for right in range(n):
        counts[s[right]] = counts.get(s[right], 0) + 1
        maxf = max(maxf, counts[s[right]])
        while right-left+1 - maxf > k: 
            counts[s[left]] -= 1
            left += 1
        res = max(res, right-left+1)
    return res

s = "AABCDACBBA"
k = 1
ret = longest_repeating_char_better(s, k)
print(ret)

        
