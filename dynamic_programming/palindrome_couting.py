from functools import lru_cache
def palindrome_counting(s):
    lens = len(s)
    dp = [[False]*lens for _ in range(lens)]
    ans = 0

    for i in range(lens):
        dp[i][i] = True
        ans += 1

    for i in range(lens-2, -1, -1):
    # for i in range(0, lens-2):
        # since i+1 needs to <= lens-1, so i <= lens-2
        for j in range(i+1, lens):
            # since dp[i][j] is from ith to jth, so j must >= i
            # since dp[i][i] == True, so j shall start from i+1
            # if dp[i+1][j-1] and s[i] == s[j]:
            #     dp[i][j] = True
            #     ans += 1
            if s[i] == s[j]:
                if dp[i+1][j-1] or j-i==1:
                    dp[i][j] = True
                    ans += 1
    print(dp)
    return ans

def palindrome_counting_algo_monster(s: str) -> int:
    length = len(s)
    dp = [[False]*length for _ in range(length)]
    ans = 0

    # possible string lengths: len = 1,...,length
    for l in range(1, length + 1):
        # possible starting indices: i = 0,...,length - len
        for i in range(0, length - l + 1):
            j = i + l - 1
            print(f"len = {l}, i = {i}, j = {j}")
            # check for the condition as mentioned in the solution that
            # the interval [i + 1, j - 1] is a palindrome and for matching characters
            if (l <= 2 or dp[i+1][j-1]) and s[i] == s[j]:
                dp[i][j] = True
                ans += 1
    return ans

@lru_cache(None)
def palindrome_counting_dfs(s):
    def is_panlindrome(st):
        return st == st[::-1]

    def dfs(start_index, path, res):
        # use a set for res, then record the [start_index, end_index] of a palindrome to it
        # then we have all results and also counts
        if start_index == len(s):
            # res.append(path[:])
            for x in path:
                res.add(x)
            return
        
        for i in range(start_index+1, len(s)+1):
            # i needs to start from start_index+1, not start_index it self
            # because we want to check s[start_index:start_indxe+1] ...
            sub_str_to_check = s[start_index:i]
            if is_panlindrome(sub_str_to_check):
                # if res is set, can't add a list as an element, but can add a tuple
                # path.append(sub_str_to_check)
                path.append((start_index, i-1))
                dfs(i, path, res)
                path.pop()

    
    # res = []
    res = set()
    dfs(0, [], res)
    return res

def partition2(s: str) -> int:
    s_length = len(s)
    # initialize the dp array so that every index in the array with i > j is set to True
    is_palindrome = [[True] * (s_length + 1) for _ in range(s_length)]
    partition_count = [0] * s_length

    # loop through the array first iterating through the possible string lengths then the possible starting indices
    for length in range(1, s_length):
        for i in range(s_length - length):
            j = i + length
            # check that the interval [i + 1, j - 1] is a palindrome and for matching characters
            is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
    
    partition_count[0] = 1
    # loop backwards checking if the particular interval is a palindrome, if it is
    # then add the number of possible partitions up to the lower bound of the interval
    for i in range(1, s_length):
        for j in range(i, 0, -1):
            if is_palindrome[j][i]:
                partition_count[i] += partition_count[j - 1]
        # check edge case that the whole interval is a palindrome itself
        # not the whole interval, but the interval from 0 to end
        # such as ab, aba, abab etc.
        if is_palindrome[0][i]:
            partition_count[i] += 1

    print(partition_count)
    return partition_count[s_length - 1]

# s = "dfxferlmjz"
# s = "aab"
s = "abab"
# s = "abbcece"
# ret = palindrome_counting(s)
ret = palindrome_counting_algo_monster(s)

# ret = palindrome_counting_dfs(s)
# ret = partition2(s)
# print(ret)
