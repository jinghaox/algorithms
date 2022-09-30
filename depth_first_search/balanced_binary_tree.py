from pretty_print_bt import BT, print_bt, pretty_print_bt, generate_tree_list
def is_balanced(root):
    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) +1
    
    return dfs(root) != -1


arr = [5, 7, 3, 'x', 'x', 8, 'x', 'x', 6, 'x', 'x']
arr_str = "1 2 3 x x 4 x 6 x x 5 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
pretty_print_bt(bt.root)
ret = is_balanced(bt.root)
print(ret)