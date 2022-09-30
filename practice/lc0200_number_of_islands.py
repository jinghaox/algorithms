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
                # for first (0,0), we got visited = {(0, 1), (2, 1), (0, 0), (3, 1), (1, 1), (0, 3), (2, 0), (0, 2), (1, 0)}
                # means those nodes have been visted, they are connected to (0,0)
                # so for next (0,1), since it's already in visited, so we skip it
                # only when we found (3,4)=="1" and not in visited, we need to bfs it, and add islands by 1
                islands += 1
    return islands

grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "0", "1", "0"]]
ret = num_of_islands(grid)
print(ret)