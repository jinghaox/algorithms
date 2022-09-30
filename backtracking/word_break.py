def word_break(s, words):
    def dfs(start_index):
        print(s[start_index:])
        if start_index == len(s):
            return True
        
        for i in range(len(words)):
            # need to check from s[start_index:]
            print(f"checking with {words[i]} at {i}")
            if s[start_index:].startswith(words[i]):
                if dfs(start_index + len(words[i])):
                    return True
        return False
    return dfs(0)

def word_break_with_memo(s, words):
    memo = {}
    def dfs(start_index):

        # this is must-have, otherwise, we don't have initialization value at the end
        if start_index == len(s):
            print(f"start_index = {start_index}")
            memo[start_index] = True
            print(memo)
            return True

        if start_index in memo:
            return memo[start_index]
        
        ok = False
        for w in words:
            if s[start_index:].startswith(w):
                if dfs(start_index + len(w)):
                    ok = True
                    break
        
        if ok:
            memo[start_index] = True
            print(memo)
            return True
        else:
            return False

        # above can be simplified to
        # but actually we don't need to save false elements

        # memo[start_index] = ok
        # return ok

    ret = dfs(0)
    print(memo)
    return ret



s = "algomonster"
words = ["monster", "algo"]
# words = ["algo", "monster"]
# s = "aaab"
# words = ["a", "aa", "aaa"]
ret = word_break_with_memo(s, words)
print(ret)
