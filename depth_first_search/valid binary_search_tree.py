from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list

def valid_bst(root):
    def dfs(node, min_v, max_v):
        if not node:
            return True  # empty node is always a valid bst, return True
        if not (min_v <= node.val <= max_v):
            return False
        return dfs(node.left, min_v, node.val) and dfs(node.right, node.val, max_v)
    return dfs(root, float('-inf'), float('inf'))

arr_str = "6 4 3 x x 8 x x 8 x x"  # False
arr_str = "6 4 3 x x 5 x x 8 x x"  # True
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
ret = valid_bst(bt.root)
print(ret)