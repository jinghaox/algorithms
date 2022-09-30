from shutil import move
from typing import List

from psutil import swap_memory

def remove_duplicates_mine(arr: List[int]) -> int:
    slow = 0
    fast = 1

    while fast < len(arr):
        if arr[fast] == arr[fast-1]:
            fast += 1
        else:
            slow += 1
            arr[slow] = arr[fast]
            fast += 1
    return slow + 1

def remove_duplicates(arr: List[int]) -> int:
    slow = 0
    fast = 0  # this one can start from 0

    # we can use for loop here, because fast always steps
    # while fast < len(arr):
    #     # we can actually compare with slow, not fast-1
    #     # so no need to worry about edge
    #     if arr[fast] == arr[slow]:
    #         fast += 1
    #     else:
    #         slow += 1
    #         arr[slow] = arr[fast]
    #         fast += 1

    # better one
    # f
    # 0 0 1 1
    # s

    #     f
    # 0 0 1 1
    # s

    # then slow+1 first
    #     f
    # 0 0 1 1
    #   s

    # then swap
    while fast < len(arr):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
            # swap is also fine, but not necessary
            # arr[slow], arr[fast] = arr[fast], arr[slow]
        fast += 1

    return slow + 1

def move_zeros_mine(nums):
    # slow and fast
    # move fast until it sees a non-zero
    # move slow until it sees a zero
    # swap them
    # repeat
    slow = 0
    fast = 0
    while fast < len(nums) and nums[fast] !=0:
        fast += 1
    while fast < len(nums):
        while fast < len(nums) and nums[fast] == 0:
            fast += 1
        while fast < len(nums) and nums[slow] != 0:
            slow += 1
        if fast < len(nums):
            nums[slow], nums[fast] = nums[fast], nums[slow]
    
    if nums[0] == 0:
        return []
    return nums[:slow+1]

def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        # fast always moves by 1
        # slow moves 1 only when nums[fast] != 0
        # 
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            # we can further improve it by checking fast!=slow
            # if fast != slow:
            #     nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    # while loop solution
    # when nums[fast] ==0, move 'fast' only by 1
    # when nums[fast] !=0, move 'slow' by 1 until it sees 0, then also move 'fast', before this, swap them
    # this means when we swap them, 'slow' already points to the first 0

    # similar to remove_duplicates, but pay attention to slow+=1, here's it's after swap
    # but in remove_duplciates, it's before placing (or swap) 
    # while fast < len(nums):
    #     if nums[fast] != 0:
    #         nums[slow], nums[fast] = nums[fast], nums[slow]
    #         slow += 1
    #     fast += 1

    return nums[:slow]

def move_zeros_by_copy(nums: List[int]) -> None:
    # copy to new array
    nonzeros = []
    for n in nums:
        if n != 0:
            nonzeros.append(n)
    print(nonzeros)
    # copy back
    i = 0
    while i < len(nonzeros):
        nums[i] = nonzeros[i]
        i += 1
    print(nums)
    # fill rest with zeros
    while i < len(nums):
        nums[i] = 0
        i += 1
    print(nums)

def move_zeros_without_copy(nums):
    i = 0
    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums

def is_palindrome_mine(s: str) -> bool:
    # algomonster (below) is faster, uses while loop inside
    l, r= 0, len(s)-1
    while l < r:
        if not s[l].isalnum():
            l += 1
        if not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
        
    return True

def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): # Note 1, 2
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower(): # ignore case
            return False
        l += 1
        r -= 1
    return True

if __name__ == '__main__':

    # arr = [1,1,1,1,1] 
    # arr = [1,2,3] 
    arr = [0,0,1,1,1,2,2]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))

    # arr = [1,0,2,0,0,7,0,9,0]
    # arr = [0, 0, 1,0,2,0,0,7,0,9,0]
    # arr = [0, 0, 0]
    arr = [3,1,0,1,3,8,9]
    # ret = move_zeros(arr)
    # ret = move_zeros_by_copy(arr)
    ret = move_zeros_without_copy(arr)
    print(ret)
