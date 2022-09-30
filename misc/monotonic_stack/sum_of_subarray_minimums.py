from typing import List

def sum_subarray(weights: List[int]) -> int:
    stack = []
    sum = 0
    curSum = 0
    for curValue in weights:
        curCount = 1
        while stack:
            if stack[-1][0] < curValue:
                break
            popped_value, popped_count = stack.pop()
            curCount += popped_count
            curSum -= popped_value * popped_count

        stack.append((curValue, curCount))
        curSum += curValue * curCount
        sum += curSum
    return sum

weights = [1,3,2]
res = sum_subarray(weights)
print(res)
