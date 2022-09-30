from typing import List

def feasible(newspapers: List[int], coworkers: int, val: int) -> bool:
    # sum to keep track of current time for the current coworker, split to keep track of the number of coworkers used thus far
    total, split = 0, 0
    for num in newspapers:
        # if one newspaper time exceeds that of our selected time then it is impossible to fulfill the time requirement we set
        if num > val:
            return False
        # check if current sum is greater than our desired time
        if total + num > val:
            total = 0
            split += 1
        total += num
    # edge case to check if we needed an extra coworker at the end
    if total != 0:
        split += 1
    # check if the number of coworkers we used is less than the desired amount
    return split <= coworkers

def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    low, high = 0, 1000000001
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers, coworkers, mid):
            high = mid - 1
        else:
            low = mid + 1
    return high + 1

newspapers = [7,2,5,10,8]
coworkers = 2
ret = newspapers_split(newspapers, coworkers)
print(ret)