import sys
from collections import deque
sys.path.append("/py_code/algomonster/depth_first_search")
print(sys.path)
from pretty_print_bt import BT, print_bt

def bt_min_depth_dfs(root):
    def dfs(node, res):
        if node is None:
            return -1 

        if node.left is None and node.right is None:
            return 0

        if node.left is None:
            return 1 + dfs(node.right, res)
        elif node.right is None:
            return 1 + dfs(node.left, res)

        return min(dfs(node.left, res), dfs(node.right, res)) + 1

    return dfs(root, 0)

def bt_min_depth_bfs(root):
    # level is 0, 1, 2
    q = deque([root])
    min_depth = 0
    while q:        
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            if node.left is None and node.right is None:
                return min_depth
            for x in (node.left, node.right):
                if x is not None:
                    q.append(x)
        min_depth += 1
    return min_depth
        
def minimumDepth(curr):
    # Null node has 0 depth.
    # root node depth is 1, then 2, 3, 4
    # so in order to align with bfs algorithm, we need to change null node's level to -1, and root's level to 0
    # i.e. line 46 return -1, line 50 return 1
    if curr == None:
        return -1 

    # Leaf node reached.
    if curr.left == None and curr.right == None:
        return 0

    # Current node has only right subtree.
    # here actually already has curr.left != None or curr.right != None
    if curr.left is None:  
        # this means depth of curr.left is 0
        return 1 + minimumDepth(curr.right)

    # Current node has only left subtree.
    elif not curr.right:
        return 1 + minimumDepth(curr.left)

    # if none of the above cases, then recur on both left and right subtrees.
    return 1 + min(minimumDepth(curr.left), minimumDepth(curr.right))

def bt_min_depth_recur(root):
    if root is None:
        return -1
    if root.left is not None and root.right is not None:
        return 1 + min(bt_min_depth_recur(root.left), bt_min_depth_recur(root.right))
    elif root.left:  # this means the node is NOT a leaf, but has left children
        return 1 + bt_min_depth_recur(root.left)
    else:
        return 1 + bt_min_depth_recur(root.right)

def bt_max_depth_recur(root):
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        return 1 + max(bt_max_depth_recur(root.left), bt_max_depth_recur(root.right))
    elif root.left:  # this means the node is NOT a leaf, but has left children
        return 1 + bt_max_depth_recur(root.left)
    else:
        return 1 + bt_max_depth_recur(root.right)

def bt_max_depth(root):
    def dfs(node):
        if node is None:
            return 0
        return 1 + max(dfs(node.left), dfs(node.right))
    
    return dfs(root)

bt = BT()
nums = [1,2,4,'x',7,'x','x',5,'x','x',3,'x',6,'x','x']
# nums = [1,2,4,'x',7,'x','x',5,'x','x',3,'x','x']
bt.build_tree(iter(nums), int)
ret = bt_min_depth_dfs(bt.root)
print(ret)
ret = bt_min_depth_bfs(bt.root)
print(ret)
ret = minimumDepth(bt.root)
print(ret)
ret = bt_min_depth_recur(bt.root)
print(ret)

print('max depth')
ret = bt_max_depth(bt.root)
print(ret)
ret = bt_max_depth_recur(bt.root)
print(ret)