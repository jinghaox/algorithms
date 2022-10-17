import collections
def num_of_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    visited = set() # we can use 2d-array, but here use set

    islands = 0 

    def bfs(r, c):
        q = collections.deque()
        visited.add((r, c))
        q.append((r,c))

        while q:  # while q is not empty, we are expanding the island
            row, col = q.popleft()
            # check adjacent
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = row+dr, col+dc 
                if ((nr) in range(rows) and
                    (nc) in range(cols) and
                    grid[nr][nc] == "1" and
                    (nr, nc) not in visited):
                    q.append((nr, nc))
                    visited.add((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                # using bfs
                bfs(r, c)  # here bfs updated the visited
                # this means when the starting node is "1", after bfs all nodes for (r,c), then we increase islands by 1
                # for first (0,0), we got visited = {(0, 1), (2, 1), (0, 0), (3, 1), (1, 1), (0, 3), (2, 0), (0, 2), (1, 0)}
                # means those nodes have been visted, they are connected to (0,0)
                # so for next (0,1), since it's already in visited, so we skip it
                # only when we found (3,3)=="1" and not in visited, we need to bfs it, and add islands by 1
                islands += 1
    print(visited)
    return islands


def num_of_islands_mock(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    num_islands = 0
    def bfs(r, c):
        q = collections.deque()
        q.append((r,c))
        visited.add((r,c))
        while q:
            row, col = q.popleft()  #popleft is bfs, pop is dfs iteratively
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                new_r, new_c = row+dr, col+dc
                if (0 <= new_r < rows and     # here must check new_r first, ow, grid[new_r][new_c] may not be valid
                    0 <= new_c < cols and     # neetcode is using new_r in range(rows)
                    (new_r, new_c) not in visited and 
                    grid[new_r][new_c] == '1'):

                    q.append((new_r, new_c))
                    print((new_r, new_c))
                    visited.add((new_r, new_c))

    # needs to check every node
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r,c)
                num_islands += 1
    return num_islands


def num_of_islands_dfs(grid):
    rows, cols = len(grid), len(grid[0])
    num_of_islands = 0
    visited = set()
    def dfs(i, r, c):  # no need of i
        # if i == rows*cols -1:
        #     return
        if (grid[r][c] == '1' and (r,c) not in visited):
            print((r,c))
            visited.add((r, c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                if r+dr in range(rows) and c+dc in range(cols):
                    dfs(i+1, r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                dfs(0, r,c)
                num_of_islands += 1

    return num_of_islands

# grid = [["1", "1", "1", "1", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "1", "0", "1", "0"]]
grid = [["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]
ret = num_of_islands_dfs(grid)
print(ret)