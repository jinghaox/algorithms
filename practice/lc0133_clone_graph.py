class Node:
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    # need a new data structure hashmap to save nodes have been cloned
    oldToNew = {}
    def clone_dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        node_copy = Node(node.val)
        oldToNew[node] = node_copy
        for nei in node.neighbors:
            # after dfs, need to update copy's neighbors
            node_copy.neighbors.append(clone_dfs(nei))
        return node_copy
    return clone_dfs(node) if node else None


def cloneGraph_alternate(self, node: 'Node') -> 'Node':
    # need a new data structure hashmap to save nodes have been cloned
    oldToNew = {}
    def clone_dfs(node):
        # we can return None here, or return None when calling clone_dfs like above
        if node is None:
            return None
        if node in oldToNew:
            return oldToNew[node]
        node_copy = Node(node.val)
        oldToNew[node] = node_copy
        for nei in node.neighbors:
            # after dfs, need to update copy's neighbors
            node_copy.neighbors.append(clone_dfs(nei))
        return node_copy
    return clone_dfs(node)