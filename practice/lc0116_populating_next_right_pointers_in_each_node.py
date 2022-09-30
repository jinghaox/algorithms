from typing import List
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class BT:
    def __init__(self):
        self.root = None
    
    def build_tree(self, nums):
        def dfs(nums):
            val = nums.pop(0)
            if val == 'x':
                return None
            left = dfs(nums)
            right = dfs(nums)
            return Node(val, left, right )
        self.root = dfs(nums)

def level_order_traversal(root):
    # queue.Queue is intended for different thread to comm using queued msg/data, thread safe
    # collection.deque is the datastructure of queue 
    res = []
    # q = deque([root])
    q = deque()
    q.append(root)
    while len(q) > 0:
        n = len(q)
        level = []
        # here's the trick, use n controls how many items to iterate, since q is changed afterwards
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res 

def connect(root):
    # BFS: but this needs space O(n/2) = O(n)
    queue = []
    queue.append(root)
    while queue:
        lens = len(queue)
        # here we use i to control elements in the queue for each level
        # for other levels elements, they have been appended to the queue, but we don't check them
        for i in range(lens):
            # for each value before the last one, we link it to next node
            # for the last one, we link it to none
            # then we pop it out, and append its children to queue
            if i < lens-1:
                queue[0].next = queue[1]
            else:
                queue[0].next = None
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        # queue[0].next = None
        # node = queue.pop(0)
        # if node.left: queue.append(node.left)
        # if node.right: queue.append(node.right)

    return root

def connect_tricky(root):
    cur, nxt = root, root.left if root else None
    while cur and nxt:
        cur.left.next = cur.right
        # only if cur.next is not None we can assign its next node's left to its right node's next
        if cur.next:
            cur.right.next = cur.next.left
        
        # then shift cur node to next node in the same level
        cur = cur.next
        if not cur:
            # if cur is None, then we need to shift to next level
            cur = nxt
            nxt = cur.left  # or nxt = nxt.left
    return root
        


bt = BT()
# build tree is using dfs (in-order)
nums = [1,2,4,'x','x',5,'x','x',3,6,'x','x',7,'x','x']
# this not working for pre-order, nums = [4,'x','x',2,5,'x','x',1,6,'x','x',3,7,'x','x']
# nums = ['x', 4, 'x', 2, 'x', 5, 'x', 1, 'x', 6, 'x', 3, 'x', 7, 'x'] 
bt.build_tree(nums)
ret = level_order_traversal(bt.root)
print(ret)
output = connect_tricky(bt.root)
ret = level_order_traversal(output)
print(ret)