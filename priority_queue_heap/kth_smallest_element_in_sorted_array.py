from typing import List
from heapq import heappush, heappop

def kth_smallest_in_sorted_array(matrix, k):
    # rows = len(matrix)
    # for r in range(rows):
    #     heappush(min_heap, (matrix[r][0], matrix[r], 0))

    min_heap = []
    for rows in matrix:
        heappush(min_heap, (rows[0], rows, 0))

    res = None
    while k > 0:
        # we pop element from row
        val, row, index = heappop(min_heap)
        res = val
        index += 1
        if index < len(row): 
            # if row still has the element, we push the next index's value
            heappush(min_heap, (row[index], row, index))
        k -=1
    
    return res

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    # Keeps track of items in the heap, and their row and column numbers
    heap = [(matrix[0][0], 0, 0)]
    # Keeps track of the top of each row that is not processed
    column_top = [0] * n
    # Keeps track of the first number each row not processed
    row_first = [0] * n
    # Repeat the process k - 1 times.
    while k > 1:
        k -= 1
        min_val, row, column = heappop(heap)
        row_first[row] = column + 1
        # Add the item on the right to the heap if everything above it is processed
        if column + 1 < n and column_top[column + 1] == row:
            heappush(heap, (matrix[row][column + 1], row, column + 1))
        column_top[column] = row + 1
        # Add the item below it to the heap if everything before it is processed
        if row + 1 < n and row_first[row + 1] == column:
            heappush(heap, (matrix[row + 1][column], row + 1, column))
        print(heap)
    return heap[0][0]

def kthSmallest_easier(matrix: List[List[int]], k: int) -> int:
    if not matrix or k < 1: return
    # using a set to keep track of already processed (row, col) pairs
    s = set()
    s.add((0, 0))
    # add [val, row, col] into heap
    heap = [(matrix[0][0], 0, 0)]
    while k > 1:
        top = heappop(heap)
        row, col = top[1], top[2]
        if col+1 < len(matrix[0]) and (row, col+1) not in s:
             heappush(heap, (matrix[row][col+1], row, col+1))
             s.add((row, col+1))
        if row+1 < len(matrix) and (row+1, col) not in s:
             heappush(heap, (matrix[row+1][col], row+1, col))
             s.add((row+1, col))
        print(heap)
        k -= 1
    return heap[0][0]

matrix = [[1, 5, 9], 
          [10,11,13], 
          [12,14,15]]
k = 6
# ret = kth_smallest_in_sorted_array(matrix, k)
# ret = kth_smallest(matrix, k)
ret = kthSmallest_easier(matrix, k)
print(ret)

