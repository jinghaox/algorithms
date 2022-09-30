def longest_substr_without_repeating_chars(s):
    # two pointers
    slow = 0
    max_len = 0
    substr = []
    for fast in range(1,len(s)):
        if s[fast] in substr:
            slow = slow + substr.index(s[fast]) + 1
        else:
            max_len = max(max_len, fast-slow+1)
        substr = s[slow:fast]

    # equivalent to the following algorithm
    # for fast in range(1,len(s)):
    #     if s[fast] in s[slow:fast]:
    #         slow = slow + s[slow:fast].index(s[fast]) + 1
    #     else:
    #         max_len = max(max_len, fast-slow+1)
    return max_len

def length_of_longest_substring(s: str) -> int:
    start = 0 
    end = 0
    max_len = 0
    slide_window = {}
    while end < len(s):
        if s[end] in slide_window:
            start = max(start, slide_window[s[end]])
        else:
            max_len = max(max_len, end-start)
        slide_window[s[end]] = end
        end += 1
    return max_len

def longest_substr_using_set(s):
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

def longest_substr_using_set_easy_understand(s):
    window = set()
    l = 0
    res = 0
    longest = 0
    r = 0
    for r in range(len(s)):
    # while r < len(s):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        window.add(s[r])
        # r += 1
        longest = max(longest, r-l+1)
    return longest

# s = "abcabcdefg"
# ret = longest_substr_without_repeating_chars(s)
# ret = length_of_longest_substring(s)
s = "abcabcbb"
# ret = longest_substr_using_set(s)
ret = longest_substr_using_set_easy_understand(s)
print(ret)


