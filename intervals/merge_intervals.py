def merge_intervals_mine(intervals):

    intervals.sort()
    # intervals = sorted(intervals, key = lambda x: x[0])

    def check_overlap(it1, it2):
        return not (it2[1] < it1[0]) and not (it1[1] < it2[0])
        # return not (it2[1] < it1[0] or it1[1] < it2[0])
    
    res = []
    first = intervals[0]
    for i in range(1, len(intervals)):
        second = intervals[i]
        if check_overlap(first, second):
            first = [min(first[0], second[0]), max(first[1], second[1])]
        else:
            res.append(first)
            first = second

    # this is the simplified version of the next commented block
    if res and check_overlap(res[-1], first):
        res[-1] = [min(res[-1][0], first[0]), max(res[-1][1], first[1])]
    else:
        res.append(first)

    # if not res:
    #     res.append(first)
    # elif check_overlap(res[-1], first):
    #     res[-1] = [min(res[-1][0], first[0]), max(res[-1][1], first[1])]
    # else:
    #     res.append(first)

    return res

def merge_intervals(intervals):
    intervals.sort()

    def overlap(a, b):
        return not (b[1] < a[0] or a[1] < b[0])

    res = []
    for interval in intervals:
        if not res or not overlap(res[-1], interval):
            # this is similar to what I have above
            # if not res means res is empty, then append interval directly
            # or, res[-1] is not overlapped with interval, we can append it directly as well
            res.append(interval)
        else:
            # this means res is not empty and res[-1] has overlap with interval
            # he only updates the right edge
            # because all intervals are sorted
            # so current interval's left must > res[-1]'s left
            # so we can keep res[-1]'s left, just update right edge
            res[-1][1] = max(res[-1][1], interval[1])
            # or we can use my method
            # res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]


    return res
        

# intervals = [[2,6], [1, 3], [8, 10], [15,18]]
intervals = [[3,7], [2, 4], [7, 10], [11,18], [9, 20]]
# intervals = [[1,6], [2,3]]
# intervals = [[1,2], [3,4], [2,5]]
ret = merge_intervals(intervals)
print(ret)

