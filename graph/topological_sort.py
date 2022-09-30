from collections import deque

def count_parents(graph):
    # first initialize number of  each node's parent to be 0
    counts = { node: 0 for node in graph }
    # then for each child node, count how many parents it has
    for parent in graph:
        for child in graph[parent]:
            counts[child] += 1
    return counts


def topo_sort(graph):
    res = []
    q = deque()
    counts = count_parents(graph)
    for node in counts:
        if counts[node] == 0:
            # push the node with 0 parents into the queue
            q.append(node)
    while len(q) > 0:
        # pop each node from the queue
        node = q.popleft()
        # since the node was in the queue, so it has 0 parents, so we add it to results
        res.append(node)
        for child in graph[node]:
            # for the poped node, iterate its children, and subtract each child's parent count by 1
            counts[child] -= 1
            # if the child's parent count is 0, push it to the queue
            if counts[child] == 0:
                q.append(child)
    return res if len(graph) == len(res) else None

graph = {1:[], 2:[1], 3:[1], 4:[2], 5:[2], 6:[3]}
# graph is a map/dict, defines each node pointing to what node, it's actually parent: list of children
# same as in leetcode 207's solution, preMap
# original graph should be  [[2,1], [3,1], [4,2], [5,2], [6,3]]
ret = topo_sort(graph)
print(ret)