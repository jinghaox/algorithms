def longest_palindrome_substr(s):
    res = []
    max_len = 0

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s)  and s[left] == s[right]:
            cur_len = right - left + 1
            if cur_len > max_len:
                res = s[left:right+1]
                max_len = cur_len
            left -= 1
            right += 1

        left, right = i, i+1
        while left >= 0 and right < len(s)  and s[left] == s[right]:
            cur_len = right - left + 1
            if cur_len > max_len:
                res = s[left:right+1]
                max_len = cur_len
            left -= 1
            right += 1

    return res, max_len

def longest_palindrome_dp(s):
    dp = [[False]*len(s)]*len(s)

    res = []
    # 要反向着做，因为dp[i][j]和dp[i+1][j-1]有关，要先求出dp[i+1][j-1]的值
    # 不需要让i从len(s)-2开始，也不需要让j从i+1开始
    # 就是说，不需要初始化对角线的值为True
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = True
                res.append(s[i])
                continue

            if s[i] == s[j]:
                if dp[i+1][j-1] or j-i <=1:
                    dp[i][j] = True
                    res.append(s[i:j+1])
    return res

s = "baba"
# ret = longest_palindrome_substr(s)
# print(ret)
ret = longest_palindrome_dp(s)
print(ret)

