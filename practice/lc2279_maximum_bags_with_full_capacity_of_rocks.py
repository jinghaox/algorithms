def maximumBags(capacity, rocks, additionalRocks):
    max_bags = 0
    n = len(capacity)
    cap_diff = [capacity[i]-rocks[i] for i in range(n)]
    # [40, 5, 75, 5, 43, 25, 7, 39, 1, 15, 39, 0, 8, 7, 76, 14, 4, 50, 25, 16, 37, 1, 99, 0, 3, 66, 28, 31, 73]
    # [0, 0, 1, 1, 3, 4, 5, 5, 7, 7, 8, 14, 15, 16, 25, 25, 28, 31, 37, 39, 39, 40, 43, 50, 66, 73, 75, 76, 99]

    rocks_left = additionalRocks
    for c in sorted(cap_diff):
        rocks_left -= c
        if rocks_left <= 0:
            break
        # should increase max_bags after the check, not before, since we may over-cap the capacity
        max_bags += 1
    return max_bags


# capacity = [2,3,4,5]
# rocks = [1,2,4,4]
# additionalRocks = 2
# capacity = [10,2,2] 
# rocks = [2,2,0]
# additionalRocks = 100

capacity = [54,18,91,49,51,45,58,54,47,91,90,20,85,20,90,49,10,84,59,29,40,9,100,1,64,71,30,46,91]
rocks =    [14,13,16,44,8, 20,51,15,46,76,51,20,77,13,14,35,6, 34,34,13,3, 8,1,  1,61, 5,2, 15,18]
additionalRocks = 77
ret = maximumBags(capacity, rocks, additionalRocks)
print(ret)