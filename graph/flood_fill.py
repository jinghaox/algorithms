from typing import List
from collections import deque
def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:

    num_rows, num_cols = len(image), len(image[0])  # will be shared with nested function

    def get_neighbors(coord: List[int], color: int):
        res = []
        r, c = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            nei_row = r + delta_row[i]
            nei_col = c + delta_col[i]
            if 0 <= nei_row < num_rows and 0<= nei_col < num_cols:
                if image[nei_row][nei_col] == color:
                    res.append([nei_row, nei_col])
        return res
    
    def bfs(node):
        q = deque([node])
        n_r, n_c = node
        visited = [[False for i in range(num_cols)] for j in range(num_cols)]
        # first get the color of the root node
        color = image[n_r][n_c]
        image[n_r][n_c] = replacement
        visited[n_r][n_c] = True
        while q:
            curr_node = q.popleft()
            for neighbor in get_neighbors(curr_node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement
                q.append(neighbor)
                visited[r][c] = True
    
    bfs((r, c))
    return image

image = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
flood_fill(2,2,9,image)
print(image)




