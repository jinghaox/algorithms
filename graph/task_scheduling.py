# see code video leetcode 207, almost the same
# that one checks if couses can be scheduled successfully, used dfs
# now we use topological_sort, it's actually bfs (the only diff is we substract the parent when iterating, 
# and only push nodes with 0 parent into the queue)
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

def task_scheduling(tasks, requirements):
    graph = {node:[] for node in tasks}
    for t, pre_t in requirements:
        graph[t].append(pre_t)
    return topo_sort(graph)

# tasks = ["a", "b", "c", "d"]
# requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
tasks = [1,2,3,4,5,6]
requirements = [[2,1], [3,1], [4,2], [5,2], [6,3]]
ret = task_scheduling(tasks, requirements)
print(ret)
