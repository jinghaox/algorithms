from typing import List
def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            # if all False, then this won't be reached
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

def find_boundary_mine(arr: List[bool]) -> int:
    # 不能用mid-1|mid|mid+1是否有transition来做这道题
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if mid <= len(arr)-2 and arr[mid] != arr[mid+1]:
            return mid+1
        elif mid >=1 and arr[mid] != arr[mid-1]:
            return mid
        elif arr[mid] == True:
            right = mid-1
        elif arr[mid] == False:
            left = mid+1
        else:
            return -1
    return -1

# arr = [False,False,False]
arr = [True, True, True, True, True]
ret = find_boundary(arr)
print(ret)
