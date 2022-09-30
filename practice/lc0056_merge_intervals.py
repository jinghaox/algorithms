from hashlib import new


def merge_intervals(intervals):
    # intervals.sort(key=lambda x: x[0]) # by default is x[0]
    intervals.sort()

    def check_overlap(it1, it2):
        # if sorted, then only needs to check it1[1] < it2[0]
        return not (it1[1] < it2[0] or it2[1] < it1[0])
    
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if check_overlap(res[-1], curr):
            # res[-1] = [res[-1][0], max(res[-1][1], curr[1])]
            res[-1][1] = max(res[-1][1], curr[1])
        else:
            res.append(curr)
    return res

def insert_interval(intervals, new_interval):
    # assuming intervals is non-overlapping and sorted already
    res = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= new_interval[1]:
        # here intervals[i][1] is already > new_interval[0]
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    # now just append new_interval, since intervals end time < new_interval start time, and overlapped intervals have been processed
    res.append(new_interval)

    while i < n:
        res.append(intervals[i])
        i += 1
    return res


 
 
# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,2], [3,5], [6,7], [8, 10], [12,16]]
ret = merge_intervals(intervals)
print(ret)
new_interval = [4,8]
ret = insert_interval(intervals, new_interval)
print(ret)