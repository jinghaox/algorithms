def find_safe_states(graph):
    n = len(graph)
    safe = {}

    def dfs(i):
        if i in safe:
            return safe[i]
        # first assume i is not a safe node
        safe[i] = False
        for neigh in graph[i]:
            # if any neighbor is not safe
            if not dfs(neigh):
                return False  # or return safe[i] since it's defined as False in line 9
        # when all neighbors are safe, then set safe[i] to True
        safe[i] = True
        return safe[i]

    res = []
    for i in range(n):
        if dfs(i):
            # if it's a safe node
            res.append(i)
    print(safe)

    return res

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
ret = find_safe_states(graph)
print(ret)
