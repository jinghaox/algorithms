from heapq import heappush, heappop, heapify

def find_kth_largest(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap) 
            heappush(min_heap, nums[i])
    
    # res = heappop(min_heap)
    res = min_heap[0]
    return res

def find_kth_largest_maxheap(nums, k):
    nums = [-x for x in nums]
    heapify(nums)

    for _ in range(k-1):
        heappop(nums)
    
    return -1*nums[0]
    

# nums = [3,2,1,5,6,4]
# k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
# ret = find_kth_largest(nums, k)
ret = find_kth_largest_maxheap(nums, k)
print(ret)