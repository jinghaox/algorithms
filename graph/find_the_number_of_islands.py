from collections import deque
def find_number_of_ones(grid):
    # what I made is actually getting number of 1s in the grid
    # but the question is asking for nuymber of islands
    # the algorithm is:
    # if grid[i][j] ==0, continue
    # otherwise, run bfs on [i,j], which will change all neighbors from 1 to 0, and then num_islands += 1
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False for j in range(num_cols)] for i in range(num_cols)]
    num_islands = 0

    def get_neighbors(coord):
        res = []
        r, c = coord
        delta_rows = [-1, 0, 1, 0]
        delta_cols = [0, 1, 0, -1]
        for i in range(len(delta_rows)):
            nei_r = r + delta_rows[i]
            nei_c = c + delta_cols[i]
            if 0 <= nei_r < num_rows and 0 <= nei_c < num_cols:
                if grid[nei_r][nei_c] == 1:
                    res.append([nei_r, nei_c])
        return res
    
    def bfs(node):
        nonlocal num_islands
        q = deque([node])
        n_r, n_c = node
        if not visited[n_r][n_c] and grid[n_r][n_c] == 1:
            num_islands += 1
        visited[n_r][n_c] = True
        while q:
            curr_node = q.popleft()
            for neighbors in get_neighbors(curr_node):
                r, c = neighbors
                if visited[r][c]:
                    continue
                q.append([r, c])
                visited[r][c] = True
                num_islands += 1
    
    for i in range(num_rows):
        for j in range(num_cols):
            bfs([i, j])
    
    return num_islands

def find_number_of_islands(grid):
    # note: after this, grid is all 0s
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False for j in range(num_cols)] for i in range(num_cols)]
    def get_neighbors(coord):
        res = []
        r, c = coord
        delta_rows = [-1, 0, 1, 0]
        delta_cols = [0, 1, 0, -1]
        print(f"get neighbor of {r, c}")
        for i in range(len(delta_rows)):
            nei_r = r + delta_rows[i]
            nei_c = c + delta_cols[i]
            if 0 <= nei_r < num_rows and 0 <= nei_c < num_cols:
                # res.append([nei_r, nei_c])
                if grid[nei_r][nei_c] == 1 or not visited[nei_r][nei_c]:
                    print(f"{nei_r, nei_c}")
                    res.append([nei_r, nei_c])
        return res
    
    def bfs(node):
        r, c = node
        # set value to 0, means it's been visited
        # grid[r][c] = 0
        visited[r][c] = True
        q = deque([node])
        while q:
            curr_node = q.popleft()
            for neighbor in get_neighbors(curr_node):
                r, c = neighbor
                if grid[r][c] == 0 or visited[r][c]:
                    continue
                else:
                    # grid[r][c] = 0
                    visited[r][c] = True
                    q.append([r,c])

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0 or visited[r][c]:
                continue
            else:
                bfs([r, c])
                count += 1
    print(visited)
    return count





grid = [[1,1,1,0],
        [0,1,1,0],
        [1,0,0,0],
        [0,1,1,0]]

ret = find_number_of_ones(grid)
print(ret)

ret = find_number_of_islands(grid)
print(ret)
