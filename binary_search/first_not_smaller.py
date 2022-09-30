from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    # we may search the half which is not the correct range
    # but before that, we remember the previous index which is >= target
    # so even we searched the wrong half, after the loop, we can still get the index
    left = 0
    right = len(arr)-1
    res = -1
    while left <= right:
        print(f"{left} - {right}")
        mid = (left+right)//2
        # here must be <, not <=
        # because it's not smaller, means >=, so here it should be <
        if arr[mid] < target:
            left = mid + 1
        else:
            res = mid
            right = mid-1

    return res

def first_not_smaller_clumsy(arr, target):
    # if we don't change right to mid-1, but mid
    # then we need to make three changes
    # 1. left < right
    # 2. right = mid
    # 3. after while loop, check res==-1,
    # then check right edge, then left edge (must be in this order)
    left = 0
    right = len(arr) - 1
    res = -1

    while left < right:
        mid = (left + right)//2
        if arr[mid] < target:
            left = mid + 1
        else:
            res = mid
            right = mid

    if res == -1:
        if arr[-1] >= target:
            return len(arr)-1
        elif arr[0] >= target:
            return 0

    return res

def find_first_occurrance_mine(arr, target):
    left = 0
    right = len(arr)-1
    res = -1
    while left <= right:
        print(f"{left} - {right}")
        mid = (left+right)//2
        # here must be <, not <=
        # because it's not smaller, means >=, so here it should be <
        if arr[mid] < target:
            left = mid + 1
        else:
            res = mid
            right = mid-1

    if arr[res] != target:
        res = -1
    return res

def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        # his idea is better, if equals, then set ans to mid, ow, keep res=-1
        if arr[mid] == target:
            ans = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans

def find_square_root(target):
    left = 0
    right = target

    res = -1
    while left <= right:
        # mid = (left + right)//2
        # for overflow, use this
        mid = left + (right-left)//2
        if mid**2 <= target:
            res = mid
            left = mid+ 1
        else:
            right = mid - 1
    return res

def find_min_rotated(arr: List[int]) -> int:

    left = 0
    right = len(arr)-1

    # this is a patch for [3,3,1,2,3,3,3]
    while arr[left] == arr[right]:
        left += 1
    while arr[right] == arr[left]:
        right -= 1

    res = -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] <= arr[-1]:
            res = mid
            right = mid -1
        else:
            left = mid + 1
    return res


def peak_of_mountain_array(arr: List[int]) -> int:
    left = 0
    right = len(arr)-1
    res = -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] > arr[mid+1]:
            res = mid
            right = mid -1
        else:
            left = mid + 1
    return arr[res]

if __name__ == '__main__':
    # arr = [1,3,3,5,8,8,10]
    # arr = [2, 3, 5, 7, 11, 13, 17, 19]
    # target = 6
    # res = first_not_smaller(arr, target)
    # res = first_not_smaller_clumsy(arr, target)
    # arr = [4,6,7,7,7,20]
    # target = 8
    # res = find_first_occurrance_mine(arr, target)
    # print(res)
    # res = find_square_root(1111111)

    # arr = [2, 2, 2, 1, 1, 1] 
    # arr = [3, 3, 4, 1, 2, 2, 2, 3, 3]
    # res = find_min_rotated(arr)

    # arr = [0, 1, 2, 3, 3, 4, 2, 0]
    # arr = [0, 8, 10, 3, 2, 1, 0]
    arr = [2,3,2]
    res = peak_of_mountain_array(arr)
    print(res)
