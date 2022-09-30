from collections import deque
def knight_minimum_moves(x, y):
    # since it's infinite grid, we don't use array but set to save visited information
    visited = set()
    # for set(), we can only add tuples to it, not list
    def get_jump_pos(coord):
        res = []
        r, c = coord
        delta_rows = [-2, -1, 1, 2, 2, 1, -1, -2]
        delta_cols = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(len(delta_rows)):
            n_r = r + delta_rows[i]
            n_c = c + delta_cols[i]
            res.append((n_r, n_c))
        return res

    def bfs(start):
        r, c = start
        q = deque([start])

        steps = 0
        while q:
            # first we check (0, 0), if it is (x,y), of course not, steps += 1
            # then we add its all neighbors of it to the queue
            # then we check all elements in the queue, if any of them is (x, y), and steps += 1
            # continue, until we reach (x, y)
            for _ in range(len(q)):
                # we update q later, but here _ only iterates over the original q
                # first q's len is 1 (only has [start])
                # then q is updated to have 8 elements
                # then _ loops from 0 to 7, although q is continuously increasing
                curr_node = q.popleft()
                r, c = curr_node
                if r == x and c == y:
                    return steps
                for neighbor in get_jump_pos(curr_node):
                    # print(f'{neighbor}')
                    if neighbor in visited:
                        continue
                    else:
                        q.append(neighbor)
                        visited.add(neighbor)
            steps += 1

    return bfs((0,0))

def minKnightMoves(x: int, y: int) -> int: 
    possible_moves = lambda x, y: [[x-2, y-1], [x-1, y-2]] 
    memo = dict() 
    def dfs(x:int, y:int)->int: 
        x, y = abs(x), abs(y)
        if (x, y) in memo:
            return memo[(x,y)]
        if x == 0 and y == 0:
            return 0
        if x+y == 2:  
            # why do we need this? because for (0,2), (1,1), and (2,0), we know it needs 2 steps, so we add them directly
            # we can't use dfs to get them, since e.g. dfs(0,1) -> dfs(2,0), if we continue, it is dfs(2-2, 0-1) = dfs(0, 1) again
            # it's endless
            return 2
        memo[(x, y)] = min(dfs(x-2, y-1), dfs(x-1, y-2)) + 1
        return memo[(x, y)]
    
    return dfs(x, y)
ret = knight_minimum_moves(2, 112)
print(ret)

ret = minKnightMoves(0, 1)
print(ret)



