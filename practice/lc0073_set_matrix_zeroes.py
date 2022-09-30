def set_matrix_zeroes(matrix):
    # mine algorithm works, haha
    rows = len(matrix)
    cols = len(matrix[0])

    q = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                q.append([i,j])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 and [i,j] in q:
                for m in range(cols):
                    matrix[i][m] = 0
                for n in range(rows):
                    matrix[n][j] = 0

def set_matrix_zeroes_algm(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    temp = False  # special storage for matrix[0][0]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j > 0:
                    matrix[0][j] = 0
                else:
                    temp = True
    print(matrix)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] =0 
    if temp == True:
        for i in range(rows):
            matrix[i][0] = 0

    

                


# matrix = [[1,1,1], [1,0,1], [1,1,1]]
# matrix = [[1,1,1], 
#           [1,0,1], 
#           [1,1,0]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,0,3]]
set_matrix_zeroes_algm(matrix)
print(matrix)