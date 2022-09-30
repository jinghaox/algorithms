import heapq
def car_pooling(trips, capacity):
    # this is O(nlogn)
    # sort is O(nlogn) and heap is also O(nlogn)
    trips.sort(key = lambda t: t[1]) # sort trips by the element at index 1
    min_heap = []   # [end, numPassengers]
    cur_passengers = 0
    for t in trips:
        num_pass, start, end = t
        while min_heap and min_heap[0][0] <= start:
            for i in range(len(min_heap)):
                print(min_heap[i])
            cur_passengers -= min_heap[0][1]
            heapq.heappop(min_heap)
        cur_passengers += num_pass
        if cur_passengers > capacity:
            return False
        heapq.heappush(min_heap, [end, num_pass])
    return True

def car_pool(trips, capacity):
    trips.sort(key = lambda t: t[1])
    mheap = []  # I can save each trip, although waste some space
    # [num_p, start, end]
    # the problem of this is: minheap sort elements by the first item of each element 
    # so now it's sorted by num_p, not end
    cur_pass = 0
    for t in trips:
        num_p, start, end = t
        while mheap and mheap[0][0] <= start:
            for i in range(len(mheap)):
                print(mheap[i])
            cur_pass -= mheap[0][1]
            heapq.heappop(mheap)
        cur_pass += num_p
        if cur_pass > capacity:
            return False
        heapq.heappush(mheap, [end, num_p, start])
    return True



def car_pooling_brute_force(trips, capacity):
    # the limitation is trips.length <= 1000
    passenger_change = [0]*1001
    for t in trips:
        num_pass, start, end = t
        passenger_change[start] += num_pass
        passenger_change[end] -= num_pass
    cur_pass = 0
    for i in range(1001):
        cur_pass += passenger_change[i]
        if cur_pass > capacity:
            return False
    return True


# trips = [[2,1,5], [3,5,7]]
trips = [[7,5,6],[6,7,8],[10,1,6]]
capacity = 16 
trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
capacity = 23
# ret = car_pooling(trips, capacity)
ret = car_pool(trips, capacity)
print(ret)
