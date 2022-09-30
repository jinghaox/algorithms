from typing import List
from collections import Counter

def longest_substring_without_repeating_characters_intuitive(s: str) -> int:
    # this is O(N^2), even we have improvement
    n = len(s)
    longest = 0
    for start in range(n):
        for end in range(n):
            sub = s[start : end + 1]
            print(sub)
            if len(set(sub)) == len(sub):
                # this means the sub has no repeatings
                # but if it happens, then we don't need to continue
                longest = max(longest, end + 1 - start)
            else:
                # this is my improvement
                break
    return longest

def longest_substring_mine(s):
    # this uses slicing and index, not good
    slow = 0
    fast = 0
    max_len = 0
    while fast < len(s):
        if s[fast] in s[slow:fast]:
            slow = slow + s[slow:fast].index(s[fast]) + 1
        else:
            max_len = max(max_len, fast-slow+1)
        fast += 1
    
    return max_len

def longest_substring_without_repeating_characters(s: str) -> int:
    n = len(s)
    longest = 0
    l = r = 0
    window = set()
    while r < n:
        if s[r] not in window:
            window.add(s[r])
            r += 1
        else:
            window.remove(s[l])
            l += 1
        longest = max(longest, r - l)
    return longest

def longest_substring_2(s: str) -> int: 
    # this one moves left to the existing element in the window + 1
    # so max_len = right-left+1
    left = res = 0 
    window = {} 
    for right, ch in enumerate(s): 
        if ch in window: 
            # need to take max
            left = max(left, window[ch] + 1)
            print(left)
        res = max(res, right - left + 1) 
        window[ch] = right 
    return res

def length_of_longest_substring(s: str) -> int:
    # this one doesn't move start to the existing element in the window + 1
    # so max_len = end - start
    start = 0 
    end = 0
    max_len = 0
    slide_window = {}
    while end < len(s):
        if s[end] in slide_window:
            # must take max of start and slide_window[s[end]]
            # reason:
            # for abba, start=2, end = 3
            # slide_window: {a:0, b:2}
            # now slide_window[s[end]] = slide_window[a] = 0
            # but start = 2, we need to let start to be 2, 
            # can't let start back off
            start = max(start, slide_window[s[end]])
            print(start)
        slide_window[s[end]] = end
        if end-start > max_len:
            max_len = end-start
        end += 1
    return max_len

def find_all_anagrams_mine(original: str, check: str) -> List[int]:
    def is_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)

    check_set = [c for c in check]
    window_set = [c for c in original[:len(check_set)]]
    res = []
    for i in range(len(check_set), len(original)+1):
        if is_anagrams(check_set, window_set): 
            res.append(i - len(check_set))
        if i < len(original):
            window_set.append(original[i])
            window_set.pop(0)
    return res

def find_all_anagrams(original: str, check: str) -> List[int]:

    original_len, check_len = len(original), len(check)

    # first check corner case
    if original_len < check_len:
        return []

    res = []
    # stores the frequency of each character in the check string
    check_counter = [ 0 ] * 26
    # stores the frequency of each character in the current window
    window = [ 0 ] * 26
    a = ord('a')  # ascii value of 'a'
    # first count check and first window
    for i in range(check_len):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1
    if window == check_counter:
        res.append(0)

    # then start interation from check_len, same as mine
    for i in range(check_len, original_len):
        # remove the first char from window, the indexing is also same as mine
        window[ord(original[i - check_len]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            res.append(i - check_len + 1)
    return res

s = "adcecabb"
ret = longest_substring_without_repeating_characters(s)
print(ret)

# ret = longest_substring_2(s)
# print(ret)
# ret = length_of_longest_substring(s)
# print(ret)

# s = "cbaebabacd"
# check = "abc"
# # s = "abab"
# # check = "ab"
# ret = find_all_anagrams(s, check)
# print(ret)