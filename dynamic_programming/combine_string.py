def combine_string (s1: str, s2: str, s3: str):
    if len(s1) + len(s2) != len(s3):
        return False

    # dp = []
    # for i in range(len(s1) + 1):
    #     dp.append([])
    # # loop through both strings and initialize dp array, we use a 1-indexed array so for our dp array we start at index 1 as opposed to 0 for strings and lists, this is so we don't go out of bounds when we subtract indices
    # for i in range(len(s1) + 1):
    #     for j in range(len(s2) + 1):
    #         dp[i].append(0)
    # print(dp)
    
    dp = [[0 for _ in range(len(s2)+1)] for y in range(len(s1)+1)]

    dp[0][0] = 1

    # only use s1[:i] to make s3[:i], s2 = ''
    # 因为是1-index based，所以从1开始iterate
    for i in range (1, len(s1) + 1):
        if s1[i - 1] == s3[i - 1]:
            dp[i][0] = True
        else: # stop as soon as prefixes don't match
            break
    print(dp)
    # only use s2[:i] to make s3[:i], s1 = ''
    for i in range (1, len(s2) + 1):
        if s2[i - 1] == s3[i - 1]:
            dp[0][i] = True
        else: # stop as soon as prefixes don't match
            break
    # loop through both strings and update dp using logic explained above
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]:
                dp[i][j] = True
            if dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]:
                dp[i][j] = True
    for i in range(len(dp)):
        print(dp[i])
    return dp[len(s1)][len(s2)]

s1 = "ace"
s2 = "bdf"
s3 = "abcdef"
ret = combine_string(s1, s2, s3)
print(ret)
