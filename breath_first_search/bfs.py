from typing import List
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res 

def print_bt_with_level(lst):
    # first restructure the lst
    output = {}
    lens = len(lst)
    for k,v in enumerate(lst):
        output[k] = lens - k - 1 
    
    indent = '\t' 
    for k,v in enumerate(lst):
        for x in v:
            print(f"{indent*output[k]}{x}", end=" ")
        print("")

def level_order_traversal_mine(root):
    # save node's value and left/right into queue
    res = []
    # q = deque([root])
    q = deque()
    q.append([root, 'root'])
    while len(q) > 0:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append([node[0].val, node[1]])
            if node[0].left:
                q.append([node[0].left,'left'])
            if node[0].right:
                q.append([node[0].right,'right'])
        res.append(level)
    return res 

def print_bt_with_level_new(lst):
    # first create a dictionary with inversed level number 
    output = {}
    lens = len(lst)
    for k,v in enumerate(lst):
        output[k] = lens - k - 1 
    
    # use the inversed level number to print
    # not perfect, but ok
    indent = '\t' 
    for k,v in enumerate(lst):
        for x in v:
            if x[1] != 'right':
                print(f"{indent*output[k]}{x[0]}", end="")
            else:
                print(f"{indent*(output[k]+1)}{x[0]}", end="\t")
        print("")

def level_traversal_zigzag_mine(root):
    q = deque([root])
    res = []
    level_index = 0
    while q:
        level = []
        num = len(q)
        # !!! note, must save len(q) first, ow, q is varied, so len(q) is changed
        for _ in range(num):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if level_index%2 == 0:
            res.append(level)
        else:
            res.append(level[::-1])
        level_index += 1
    
    return res

def level_traversal_zigzag_different_pop(root):
    # can't use this one
    # q = [6,8,4,5]
    # q.pop() -> [6,8,4], since 5 has no children
    # q.pop() -> [6,8], but 4 has right node 7, so [6,8,7]
    # q.pop() it returns 7
    # so that's why when level_index%2 == 1, needs to use appendleft(right), then appendleft(left)
    # when we pop from right, we add new nodes to left
    # when we pop from left, we append new nodes to right
    q = deque([root])
    res = []
    level_index = 0
    while q:
        level = []
        num = len(q)
        for _ in range(num):
            if level_index%2 == 0:
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            else:
                node = q.pop()
                level.append(node.val)
                if node.right: q.appendleft(node.right)
                if node.left: q.appendleft(node.left)
        res.append(level)
        level_index += 1
    
    return res


    
def zig_zag_traversal(root: Node) -> List[List[int]]:
    # algomonster's algorithm is cool, flip the flag every time
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    left_to_right = True
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]: # enqueue non-null children
                if child is not None:
                    queue.append(child)
        if not left_to_right:
            new_level.reverse() # reverse current level
        res.append(new_level)
        left_to_right = not left_to_right # flip flag
    return res


def zig_zag_traversal_other(root: Node) -> List[List[int]]: 
    # this is someone else's solution
    res = [] 
    q = deque([root])
    while q:
        level = []
        for i in range(len(q)):

            if len(res) % 2 == 0:
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            else:
                node = q.pop()
                if node:
                    level.append(node.val)
                    # he used appendleft
                    q.appendleft(node.right)
                    q.appendleft(node.left)
        if level:            
            res.append(level)

    return res

def zig_zag_traversal_insert_append(root: Node) -> List[List[int]]:
    # using insert or append for level, this also works
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    level_index = 0
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            if level_index % 2 == 0:
                new_level.append(node.val)
            else:
                new_level.insert(0, node.val)
            for child in [node.left, node.right]: # enqueue non-null children
                if child is not None:
                    queue.append(child)
        res.append(new_level)
        level_index += 1
    return res

def right_side_view(root):
    res = []
    q = deque([root])
    while q:
        lens = len(q)
        for i in range(lens):
            node = q.popleft()
            if i == lens-1:
                res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res

def right_side_view_alternate(root):
    res = []
    q = deque([root])
    while q:
        lens = len(q)
        # another way is before for loop, first append the last q's value
        # or append the first q's avlue if we call q.append(right), then q.append(left)
        res.append(q[-1].val)
        for i in range(lens):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res

def left_side_view(root):
    res = []
    q = deque([root])
    while q:
        lens = len(q)
        for i in range(lens):
            node = q.popleft()
            if i == 0:
                res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res

def find_shallowest_leaf_level(root):
    q = deque([root])
    res = None
    level = 0
    while q:
        num = len(q)
        for _ in range(num):
            node = q.popleft()
            if node.left is None and node.right is None:
                # res = node.val  # this prints the leaf's val
                res = level
                return res
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        level += 1
    return res


bt = BT()
nums = [1,2,4,'x',7,'x','x',5,'x','x',3,'x',6,'x','x']
# nums = [1,2,4,'x',7,'x','x',5,'x','x',3, 6, 'x', 'x', 8, 'x','x']
bt.build_tree(nums)

# ret = level_order_traversal(bt.root)
# print(ret)

# ret = level_order_traversal_mine(bt.root)
# print(ret)
# print_bt_with_level_new(ret)

# ret = level_traversal_zigzag_mine(bt.root)
# ret = level_traversal_zigzag_different_pop(bt.root)
# ret = zig_zag_traversal_other(bt.root)
# ret = zig_zag_traversal_insert_append(bt.root)
# print(ret)

ret = right_side_view_alternate(bt.root)
print(ret)
# ret = left_side_view(bt.root)
# print(ret)

# ret = find_shallowest_leaf_level(bt.root)
# print(ret)
