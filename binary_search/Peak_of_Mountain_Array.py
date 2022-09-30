def peak_of_mountain_array(arr):
    res = -1
    left, right = 0, len(arr)-1
    # we can patch an -inf to the end
    arr.append(float('-inf'))
    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= arr[mid+1]:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    return res

# arr = [0,1,2,3,2,1,0]
arr = [0,1,2,3]
ret = peak_of_mountain_array(arr)
print(ret)