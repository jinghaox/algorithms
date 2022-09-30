from typing import List
from collections import deque

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    def get_neighbors(node):
        return graph[node]
    
    def bfs(root, target):
        visited = set([root])
        q = deque([root])
        level = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if target == node:
                    return level
                for nbr in get_neighbors(node):
                    if nbr in visited:
                        continue
                    q.append(nbr)
                    visited.add(nbr)  # using add for set
            level += 1

    return bfs(a, b)

if __name__ == '__main__':
    # input 
    # number of vertecies: 4
    # each node's adjacent list: 
    #  1 2
    #  0 2 3
    #  0 1
    #  1
    # a: 0
    # b: 3

    # the first input goes to range(int(input()))
    # others go to for x in input.split()
    # graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    # a = int(input())
    # b = int(input())
    graph = [ [1,2], [0,2,3], [0,1], [1]]
    a = 0
    b = 3
    res = shortest_path(graph, a, b)
    print(res)
