from heapq import heappush, heappop
from typing import List
from math import sqrt

def k_closest_points_minheap(points, k):
    dist = [(x**2+y**2)**0.5 for (x, y) in points]
    data = []
    for i in range(len(points)):
        # the reason we use (dist, points) is because we need dist as the index for minheap
        # and we need to output the points
        heappush(data, (dist[i], points[i]))
    res = []
    for i in range(k):
        # res.append(heappop(data)[1])
        # or output heappop like this
        dt, pt = heappop(data)
        res.append(pt)
    return res    


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    # this is using maxheap, not minheap

    # first push only k of them, assume they are the smallest
    # then push a new val after k+1, if it's smaller < top, then pop the top, and push it in
    # so the heap still keeps k smallest
    # repeat it until all vals have been checked, then pop all from the heap, that's what we need

    # so this means, for smallest k, we use maxheap-k
    # for highest k, we can use minheap-k
    def dist(point):
        return -sqrt(point[0] ** 2 + point[1] ** 2) # "-" for max heap

    max_heap = []
    for i in range(k):
        pt = points[i]
        heappush(max_heap, (dist(pt), pt))

    for i in range(k, len(points)):
        pt = points[i]
        # max_heap[0] is root of max heap, the point with largest distance
        # max_heap[0][0] is -distance
        if dist(pt) > max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (dist(pt), pt))

    res = []
    for _ in range(k):
        _, pt = heappop(max_heap)
        res.append(pt)

    return res

def merge_k_sorted_lists_mine(lists):
    # here the problem is, how do we know which list to pop the value
    min_heap = []
    i = 0
    res = []
    for sl in lists:
        if sl:
            heappush(min_heap,sl[0])
        res.append(heappop(min_heap))
    return res

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # we use head_index to mark and tell which node in cur_list to push
    res = []
    heap = []
    for current_list in lists:
        # we use heap to store the pool of the smallest value of each list
        # push first number of each list into the heap, this is the smallest value
        # also push current_list, and the index into it
        # we need them to know where the next number to push
        heappush(heap, (current_list[0], current_list, 0)) # 1

    while heap:
        val, current_list, head_index = heappop(heap)
        res.append(val)
        head_index += 1
        # if there are more numbers in the list, push into the heap
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))

    return res

def merge_k_sorted_lists_working(lists: List[List[int]]) -> List[int]: 
    # this one modifies the list
    # when we push, we pop the val from the list
    heap = [] 
    result = [] 
    for i in range(len(lists)): 
        # we use i to mark which list is pushing its value to heap
        heappush(heap, (lists[i].pop(0), i)) 

    while heap: 
        elem, n = heappop(heap) 
        result.append(elem) 
        if lists[n]: 
            # again, we push the val from the list, and pop it from that list as well
            heappush(heap, (lists[n].pop(0), n)) 
    # so at the end, the lists is empty
    return result

def merge_k_sorted_lists_mock(lists):
    hp = []
    res = []

    for cur_list in lists:
        heappush(hp, (cur_list[0], cur_list, 0))
    # now the initial heap has k smallest values, each val is the smallest of each list

    while hp: # pop out heap until it's empty
        # first pop the smallest in the heap
        smallest, cur_list, index = heappop(hp)
        res.append(smallest)
        # then increase index, we use this to indicate which element in the cur_list we should push
        # so we don't need to modify cur_list
        index += 1
        if index < len(cur_list):
            heappush(hp, (cur_list[index], cur_list, index))
    print(lists)
    return res

points = [[1,1],[4,4],[2,2],[3,3]]
k = 2

# ret = k_closest_points(points, k)
# ret = k_closest_points_minheap(points, k)
# print(ret)

lists = [[1, 3, 5], [2, 4, 6], [7, 10]]
# ret = merge_k_sorted_lists(lists)
# ret = merge_k_sorted_lists_mock(lists)
ret = merge_k_sorted_lists_working(lists)
print(ret)
