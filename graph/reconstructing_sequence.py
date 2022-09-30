from collections import deque
from typing import List

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    def count_parents(graph):
        counts = { node: 0 for node in graph }
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts


    def topo_sort(graph):
        seq = []
        q = deque()
        counts = count_parents(graph)
        for node in counts:
            if counts[node] == 0:
                q.append(node)
        while len(q) > 0:
            if len(q) > 1: # if there's > 1 item, then the recontruction is not unique
                return False
            node = q.popleft()
            seq.append(node)
            for child in graph[node]:
                counts[child] -= 1
                if counts[child] == 0:
                    q.append(child)
        return seq == original

    # Create the graph from the sequences
    # The orginal sequence is a permutation of the integers from 1 to n
    # n = len(original)
    # graph = { node: set() for node in range(1, 1 + n) } # nodes from 1 to n
    graph = {node: [] for node in original}
    # use set() instead of [], because it may have repeated edges from the sequences
    # such as [4,5,2,3], [2,3,7,8]
    # 4->5, 5->2, 2->3
    # 2->3, 3->7, 7->8
    # here 2->3 is repeated
    for seq in seqs:
        for i in range(len(seq) - 1): # create an edge for each adjancent pairs
            source, destination = seq[i], seq[i + 1]
            graph[source].add(destination)
    return topo_sort(graph)

# original = [1,2,3]
# seqs = [[1,2], [1,3]]  # create graph {1:{2,3}, 2:{}, 3:{}} --> counts: {1:0, 2:1, 3:1}, 2's parent is 1, 3's parent is1
original = [4,5,2,3,7,8]
seqs = [[4,5,2,3], [2,3,7,8]]
# original = [4,1,5,2,6,3]
# seqs = [[5,2,6,3], [4,1,5,2]]
res = sequence_reconstruction(original, seqs)
print('true' if res else 'false')
