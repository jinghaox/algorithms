def rotate(matrix):
    l, r = 0, len(matrix)-1
    while l < r:
        for i in range(r-l):
            t, b = l, r
            top_left = matrix[t][l+i]
            matrix[t][l+i] = matrix[b-i][l]
            matrix[b-i][l] = matrix[b][r-i]
            matrix[b][r-i] = matrix[t+i][r]
            matrix[t+i][r] = top_left
        l += 1
        r -= 1
    return matrix

matrix =[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]] 

ret = rotate(matrix)
print(ret)