def spiral_matrix(matrix):
    res = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while left < right and top < bottom:
        # get the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1


        # get the right col
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        # the reson we need to break when either left>=right or top >== bottom
        # for single column, left already >= right, we shouldn't continue to print bottom, since now top still < bottom
        # for single row, top >= bottom, we shouldn't continue to print left, since now left still < right
        # if not (top < bottom):
        if not(left < right and top < bottom):
            break


        # get the bottom row
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res

# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
#           [13,14,15,16]
#           ]
# matrix = [[7],
#           [9],
#           [6]]
matrix = [[1,2,3]]
ret = spiral_matrix(matrix)
print(ret)
