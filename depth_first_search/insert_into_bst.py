
from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list
def insert_node(root, val):
    def dfs(node, val):
        if node is None:
            return BTNode(val, None, None)
        if node.val > val:
            # can't return here directly, need to update the tree
            # 这里，我们update node.left by dfs(node.left, val), 因为我们要把val插入到node.left中去
            node.left = dfs(node.left, val)
        if node.val < val:
            node.right = dfs(node.right, val)
        return node  #所以我们不是建一个新的node，而是更新现有的node node
    return dfs(root, val)

# def format_tree(root, res):
    # if root is None:
    #     yield 'x'
    #     return
    # yield str(root.val)
    # yield from format_tree(root.left)
    # yield from format_tree(root.right)

res = []
def format_tree(root, res): 
    # 这个实际上就是serializing啊，见serialize_binary_tree.py
    # pass in res as an argument
    if root is None:
        res.append('x')
        return
    res.append(str(root.val))
    format_tree(root.left, res)
    format_tree(root.right, res)

# res = []
# def format_tree(root):
#     if root is None:
#         res.append('x')
#         return
#     res.append(str(root.val))
#     # 这个根本不对，因为format_tree没有return any node
#     # 所以后面的 if left_node根本不会被 执行
#     # 所以就相当于只call format_tree(root.left)
#     # 和上面的一样
#     left_node = format_tree(root.left)
#     right_node = format_tree(root.right)
# 
#     if left_node:
#         print('not here')
#         res.append(left_node.val)
#     if right_node:
#         print('not here')
#         res.append(right_node.val)
#     return

arr_str = "8 5 2 x 3 x x 6 x x 10 x 14 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
insert_node(bt.root, 9)
# format_tree(bt.root, res)
format_tree(bt.root)
print(res)