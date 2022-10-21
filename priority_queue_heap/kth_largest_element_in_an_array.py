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
    
def find_kth_largest_quick_select(nums, k):
    min_pointer = 0
    max_pointer = len(nums) - 1
    while min_pointer < max_pointer:
        pivot = nums[max_pointer]
        swap_left = min_pointer
        swap_right = max_pointer
        while swap_left < swap_right:
            while swap_left < swap_right and nums[swap_left] > pivot:
                swap_left += 1
            while swap_left < swap_right and nums[swap_right] <= pivot:
                swap_right -= 1
            if swap_left < swap_right:
                nums[swap_left], nums[swap_right] = nums[swap_right], nums[swap_left]
        # here, place the largest number to the beginning of the array
        nums[swap_left], nums[max_pointer] = nums[max_pointer], nums[swap_left]
        # so the k-1 element is what we want
        if swap_left == k - 1:
            return nums[swap_left]
        elif swap_left < k - 1:
            min_pointer = swap_left + 1
        else:
            max_pointer = swap_left - 1
    return nums[min_pointer]

# nums = [3,2,1,5,6,4]
# k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
# ret = find_kth_largest(nums, k)
# ret = find_kth_largest_maxheap(nums, k)
ret = find_kth_largest_quick_select(nums, k)
print(ret)