def get_neighbors(coord, rows, cols):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            res.append((neighbor_row, neighbor_col))
    return res

rows = 3
cols = 3
res = get_neighbors([1,2], rows, cols)
print(res)

    