def longest_increasing_subseq(arr):
    # using dp
    # for each element, dp[i], iterate all nodes before i, and check which is bigger, dp[i] or dp[j]+1 
    dp = [1]*len(arr)

    max_len = 0
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    return max_len

def longest_increasing_subseq_reverse(arr):
    dp = [1]*len(arr)
    max_len = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
        max_len = max(max_len, dp[i])
    return max_len
# arr = [1,2,4,3]
arr = [10,9,2,5,3,7,101,18]
ret = longest_increasing_subseq_reverse(arr)
print(ret)