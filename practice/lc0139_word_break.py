
def word_break(s, word_dict):
    # O(n*m*n), m is the size of word_dict
    # since startswith(w) also takes O(n)
    # this will cause TLS, so we need memo
    def dfs(start_index):
        if start_index == len(s):
            return True
        for w in word_dict:
            if s[start_index:].startswith(w):
                if dfs(start_index+len(w)):
                    return True
        return False
    ret = dfs(0)
    return ret

def word_break_memo(s, wordDict):
    def dfs(start_index, memo):
        if start_index == len(s):
            return True
        if start_index in memo:
            return memo[start_index]
        
        ok = False # use this to control the normal dfs call's return, and it also updates memo
        for w in wordDict:
            if s[start_index:].startswith(w):
                ret = dfs(start_index + len(w), memo)
                if ret: 
                    ok = True
                    break
        memo[start_index] = ok
        return ok
    ret = dfs(0, {})
    return ret
        
def word_break_dp(s, wordDict):
    dp = [False]*(len(s)+1)  # has extra one False at the end, which is the base case
    dp[-1] = True  # set the base case to be True
    for i in range(len(s)-1, -1, -1):  # starts from len(s)-1, e.g. "a", ["a"], need to check the last one
        for w in wordDict:
            if len(s)-i < len(w):
                dp[i] = False  # not necessary, because it's already False
            elif s[i:i+len(w)] == w:  # here means len(s) - i >= len(w) 
                # the above can be simplified to if len(s)-i >= len(w) and s[i:i+len(w)] == w
                dp[i] = dp[i+len(w)]
                if dp[i]:
                    # no need to check all words in wordDict
                    break
    return dp[0]

s = "leetcode"
word_dict = ["leet", "co", "ode"]
# s = "catsanddog"
# word_dict = ["cats", "dog", "sand", "and", "cat"]
# s = "a"
# word_dict = ["a"]
ret = word_break(s, word_dict)
print(ret)
