def permutation(letters):
    # letters: e.g. 'abc', it's permutate itself
    # level is used to help understanding, not needed
    def dfs(path, used, res, level):
        print('-------------------')
        if len(path) == len(letters):
            # must use deep copy
            res.append(path[:])
            return
        
        for i, letter in enumerate(letters):
            print(f"i = {i} at level = {level}")
            if used[i]:
                # skip used letters
                continue
            used[i] = True
            path.append(letter)
            dfs(path, used, res, level+1)
            print('backtrack')
            path.pop()
            used[i] = False

    res = []
    dfs([], [False]*len(letters), res, 1)
    return res

def partial_permutation(letters, n):
    def dfs(path, used, res, d, n):
        # d is the depth
        if d == n:
            res.append(path[:])
        for i in range(len(letters)):  # not using enumerate
            if used[i]:
                continue
            used[i] = True
            d = d+1
            path.append(letters[i])
            dfs(path, used, res, d, n)  
            # or use dfs(path, used, res, d+1, n), then not need to backtrack d
            path.pop()
            d = d-1
            used[i] = False
    
    res = []
    dfs([], [False]*len(letters), res, 0, n)
    return res

def letter_comb_phone_number(digits):
    letter_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def dfs(path, res):
        if len(path) == len(digits):
            # digits, e.g. 56 ('jkl', 'mno'), length is 2, output is jm,jn,jo,..., also 2
            # so this can be used to exit
            res.append(''.join(path))
            return
        next_dig = digits[len(path)]  #!!! note we use len(path) count the current stage, we can use start_index instead, see dfs2
        # next_digit, first is 5, next is 6
        for c in letter_dict[next_dig]:
            path.append(c)
            # next dfs() call, will work on the next digit
            dfs(path, res)
            path.pop()
    
    def dfs2(start_index, path, res):
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        for c in letter_dict[digits[start_index]]:
            path.append(c)
            dfs2(start_index+1, path, res)
            path.pop()

    res = []
    # dfs([], res)
    dfs2(0, [], res)
    return res

def permutation_phone_number_like(letters):
    # 'abc' permutation, has no repeatitions, 
    # so it's ['abc','acb','bac','bca','cab','cba']
    # if it has repeatitions like the phone number example, then it will be
    # 'abc' -> 'abc' -> 'abc'
    # like 1->'abc', 1->'abc', 1->'abc
    # 'aaa','aab','aac','aba','abb','abc','aca','acb','acc'
    # 'baa','bab','bac','bba','bbb','bbc','bca','bcb','bcc'
    # 'caa','cab','cac','cba','cbb','cbc','cca','ccb','ccc'
    def dfs(path, used, res):
        # we can define a new argument rep(repeatition) to control the exit as well
        # now we use len(path) == len(letters) to control the exit
        # if we don't use used[i] to control the letter that can be used, then we 
        # have repeated permutations
        if len(path) == len(letters):
            res.append(''.join(path))
            return
        for i in range(len(letters)):   # or for c in letters:  append(c)
            # if used[i]:
            #     continue
            # used[i] = True
            path.append(letters[i])
            dfs(path, used, res)
            path.pop()
            # used[i] = False
    res = [] 
    dfs([], [False]*len(letters), res)
    return res

def word_break(s, words):
    # any word in the words can be used, so no extra state needed
    # we need to iterate s, so using an index
    # what to return? not to return None, but needs to return True or False
    # since we need this for a recursive call
    def dfs(index, res):
        if index == len(s):
            return True
        for word in words:
            # if s[index:].startswith(word):  
            # if don't allow to use startswith, then use slicing
            if s[index: index+len(word)] == word:
                ret = dfs(index + len(word), res) 
                if ret:
                    res.append(s[index:index+len(word)])
                    return True
                # do not return false, if using return dfs(), will return False
                # only after all words have been checked, and no True, we return False
        return False

    res = []
    dfs(0, res)
    return res

def  word_break_with_memoization(s, words):
    # for "aaaab" and ["a", "a"*2, "a"*3]
    # when index is 3, current word to check is "a"
    # s[index:index+1] is b, dfs(4) will return False after checking three word in words, 
    # so memo will be set to {4:False}
    # then for loop continues on index 3, now next word to check is "aa"
    # since s[index:index+2] = s[3:5] = "ab" != "aa", so for loop will be skipped on "aa", goes to "aaa", still skipped
    # now memo is set to {3:False, 4:False}
    memo = {}
    def dfs(index, res):
        if index == len(s):
            return True
        
        if index in memo:
            print("memo is checked")
            return memo[index]
        
        ok = False
        for word in words:
            if s[index: index+len(word)] == word:
                ret = dfs(index + len(word), res)
                if ret:
                    ok = True
                    res.append(s[index:index+len(word)])
                    break
        # if dfs returns True, then memo[index] is True
        # otherwise, after all words have been checked, memo[index] is False
        memo[index] = ok
        return ok 
    
    res = []
    ret = dfs(0, res)
    print(memo)
    print(res)
    return ret

def word_break_memo(s, words):
    memo = {}
    def dfs(start_index):
        if start_index == len(s):
            return True
        if start_index in memo:
            print("memo is checked")
            return memo[start_index]
        ok = False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ok = True
                    break
        memo[start_index] = ok
        return ok
    return dfs(0)



def palindrome_partition(s):
    def is_palindrom(st):
        # or using pythonic way
        # return st = st[::-1]
        left = 0
        right = len(st)-1
        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def dfs(index, path, res):
        if index == len(s):
            res.append(path[:])
            return

        # for i, v in enumerate(s[index:]): 
        #     sub_str_to_check = s[index:index+i+1]
        #     # i is from 0 to n-index
        #     # so it's also from index:index+0+1=index:index+1, to index:index+n-index+1 = index:n+1 
        #     if is_palindrom(sub_str_to_check):
        #         path.append(sub_str_to_check)
        #         dfs(index + i +1, path, res)
        #         path.pop()

        for i in range(index+1, len(s)+1):  # to len(s)+1, means go up to len(s)
            # this means we want to check substring starting from index and beyond
            sub_str_to_check = s[index:i]
            # from index to i, where i is index+1 to n+1
            # so it's index:index+1,  index:index+2
            if is_palindrom(sub_str_to_check):
                path.append(sub_str_to_check)
                dfs(i, path, res)
                path.pop()
        
    res = []
    dfs(0, [], res)
    return res

def combination_sum(candidates, target):
    def dfs(index, path, res, remaining):
        # shall I return 0 or return? 
        # no need to return 0, since remaining tells us what is remained for each dfs call
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            # if remaining < 0, then this res is not valid, will be discarded
            # later on, after this return, path will pop, so all numbers in path will be discarded
            # algomonster did remaining-num check inside the for loop
            print(f'invalid: {path}')
            return
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            # if remaining - candidates[i] < 0:
            #     continue
            dfs(i, path, res, remaining-candidates[i])
            # here is dfs(i), 
            path.pop()
    res = [] 
    dfs(0, [], res, target)
    return res

def sub_sets_mine(nums):
    # not working
    def dfs(index, res, path):
        if index == len(nums):
            return
        for i in range(index, len(nums)):

            path.append(nums[i])
            res.append(path[:])
            dfs(i+1, res, path)
            path.pop()

            dfs(i+1, res, path)
    res = []
    dfs(0, res, [])
    return res

def sub_sets(nums):
    def dfs(index, path, res):
        if index == len(nums):
            res.append(path[:])
            return
        dfs(index+1, path, res)
        # recursion call including nums[index]
        dfs(index+1, path + [nums[index]], res)
        # recursion call without nums[index]
    res = []
    dfs(0, [], res)
    return(res)


# ret = permutation('abc')
# print(ret)
# 
# ret = partial_permutation('abcd', 2)
# print(ret)
# 
ret = letter_comb_phone_number('23')
print(ret)
# 
# ret = permutation_phone_number_like('abc')
# print(ret)

# s = "abcd"
# words = ["a", "ab", "cd"]
# s = "aaaaaaa"
# # words = ["a", "aa", "aaa"]  # this will return 7 'a', since each time we find 'a' is working
# words = ["aaa", "aa", "a"]  # to make use of other 'aaa', reverse words
# s = "a"*140
# words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "a"*8, "a"*9, "a"*10]
# words = words[::-1]
# ret = word_break(s, words)
# print(ret)

# s = "abcd"
# # words = ["a", "abd", "b", "d"]
# words = ["a", "ab", "d", "cd"]
# s = "a"*140 + "b"  # when we have "b" at the end, then memo is checked
# words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "a"*8, "a"*9, "a"*10]
# s = "abcd"
# words = ["a", "abc", "b", "cd"]

# s = "aaaab"
# words = ["a", "a"*2, "a"*3]
# ret = word_break_with_memoization(s, words)
# # ret = word_break_memo(s, words)
# print(ret)

# ret = decode_ways_mine('235')
# ret = decode_ways('235')
# ret = decode_ways_without_memo('235')  # [2,3,5] [23, 5]
# ret = decode_ways_without_memo('11223')
# # ret = decode_ways_with_memo_and_res('11223')
# print(ret)

# s = "aab"
# ret = palindrome_partition(s)
# print(ret)

# ret = combination_sum([2,3,5], 8)
# print(ret)

# ret = sub_sets_mine('123')
# print(ret)

