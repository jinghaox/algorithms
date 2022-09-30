from collections import Counter
def get_minimum_window_mine(original, check):
    # first find the sliding window containing check
    # then move start pointer until check in not contained in sliding window
    # record the result
    # then repeat the same process
    # when find another result, check which result is lexicographically smaller

    # define two pointers
    start = 0
    end = 0

    check_len = len(check)
    original_len = len(original)
    # special case
    if original_len < check_len:
        return ""

    # count freq of each char in check 
    check_set = Counter(check)

    # initialize sliding window
    window = []

    def check_containing(d1, d2):
        # helper function to check if dict1 is contained by dict2
        # check keys first, and if having the same keys, check each key's value 
        for k, v in d1.items():
            if k not in d2 or v > d2[k]:
                return False
        return True

    # results
    res = "" 

    while end < original_len:
        # append current char to the sliding window
        window.append(original[end])
        # count the freq of each char in the sliding window
        window_set = Counter(window)

        if check_containing(check_set, window_set): 
            # if "sliding window" contains all chars in "check"
            # move start pointer until window doesn't contain check set
            while check_containing(check_set, window_set): 
                window.pop(0)
                window_set = Counter(window)
            window_len = len(window)
            start = end - window_len + 1

            # get the candidate that contains "check"
            new_candidate = original[start-1:end+1]

            # when res is empty, set the candidate as the result
            if len(res) == 0:
                res = new_candidate
            else:
                # when we already have result, do two comparisons
                # 1. compare the length of the new candidate with the exisiting result
                # 2. get the lexicological smaller candidate
                if len(new_candidate) <= len(res):
                    res = min(res, new_candidate)
        end += 1

        #     end += 1
        # else:
        #     end += 1

    return res
        
def get_minimum_window(original: str, check: str) -> str:
    # Counts the number of each character of "check"
    check_count = Counter(check)
    # Counts the number of each character in the sliding window
    window_count = {}
    # Count the number of entries in "check_count" that is smaller than or equal to
    # that in "window_count"
    # If "satisfy_count" is equal to the number of entries in "check_count",
    # that window contains "check". We then just need to check if its the minimum.
    satisfy_count = 0
    original_len = len(original)
    # Two pointers pointing to the window (inclusive start, exclusive end)
    start_ptr = 0
    end_ptr = 0
    # The number of entries in "check_count". Used to check if "window_count" contains
    # "check_count"
    match_req = len(check_count.keys())
    # The smallest recorded string that satisfies the conditions.
    smallest_str = None
    # Change the number of "char" inside the window by "delta"
    # Automatically increase or decrease "satisfy_count" to reflect the current value.
    def delta_char(char, delta):
        nonlocal satisfy_count
        if char not in window_count:
            window_count[char] = 0
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count -= 1
        window_count[char] += delta
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count += 1
    while end_ptr < original_len:
        # Moves the end pointer until it contains "check" or it reaches the end
        while end_ptr < original_len and satisfy_count < match_req:
            delta_char(original[end_ptr], 1)
            end_ptr += 1
        # If the window reaches the end and does not contain "check", break loop
        if end_ptr == original_len and satisfy_count < match_req:
            break
        # Otherwise, the window contains "check", so we move the start pointer
        # until it no longer does. Then, the one before failing the check is the local
        # minimal substring.
        while satisfy_count >= match_req:
            delta_char(original[start_ptr], -1)
            start_ptr += 1
        valid_window = original[start_ptr - 1 : end_ptr]
        # Compare the local minimum to the stored smallest string
        # If there is nothing stored, or the condition outlined is true, we store the string
        if smallest_str is None or (len(smallest_str) > len(valid_window)):
            smallest_str = valid_window
        elif len(smallest_str) == len(valid_window) and valid_window < smallest_str:
            smallest_str = valid_window
    return smallest_str or ""

# original = "acdbaebaecd"
# check = "abc"

original = "AEOIEAIOUAOEIAOEIIAAEIUIOUUA"
check = "AEIOU"
ret = get_minimum_window(original, check)
print(ret)
        

