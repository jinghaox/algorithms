def check_string_contains_all_binary_codes(nums,k):
    code_set = set()
    for i in range(len(nums)-k+1):
        code_set.add(nums[i:i+k])
    print(code_set)
    return len(code_set) == 2**k

nums = "00010011101"
k = 3
ret = check_string_contains_all_binary_codes(nums, k)
print(ret)