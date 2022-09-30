def most_water(height):
    left = 0
    right = len(height)-1
    max_area = 0
    while left < right:
        if height[left] < height[right]:
            max_area = max(max_area, height[left]*(right-left))
            left += 1
        else:
            max_area = max(max_area, height[right]*(right-left))
            right -= 1
    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ret = most_water(height)
print(ret)
