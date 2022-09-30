from typing import List

def feasible(weights: List[int], max_weight: int, d: int) -> bool:
    # req_days = 1
    # # the reason we need to assign max_weight to capacity is because later on,
    # # we need to reset capacity to max_weight
    # capacity = max_weight
    # i = 0
    # n = len(weights)
    # while i < n:
    #     if weights[i] <= capacity:
    #         capacity -= weights[i]
    #         i += 1
    #     else:
    #         req_days += 1
    #         capacity = max_weight
    # return req_days <= d

    # this is the same as the question of newspaper
    req_days = 1
    prev_sum = 0
    for w in weights:
        # 这个算法是，对当前w来讲，如果prev_sum+w 超过max_weight了，那么prev_sum is reset to 0
        # 天数会加1，然后，因为当前的值是w，所以要更新prev_sum to prev_sum += w，即w，因为prev_sum==0
        # 如果没有超过max_weight，那么当然要 +w
        # if prev_sum + w > max_weight:
        #     prev_sum = 0
        #     req_days += 1
        # prev_sum += w

        # the above is the same as below
        if cur_sum + w > max_weight:
            cur_sum = w
            req_days += 1
        else:
            cur_sum += w
    return req_days <= d


def min_max_weight(weights: List[int], d: int) -> bool:
    min_ptr = max(weights)
    max_ptr = sum(weights)
    boundary_index = max_ptr
    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        if feasible(weights, midpoint, d):
            boundary_index = midpoint
            max_ptr = midpoint - 1
        else:
            min_ptr = midpoint + 1
    return boundary_index

weights = [1,2,3,4,5,6,7,8,9,10]
d = 5
ret = min_max_weight(weights, d)
print(ret)