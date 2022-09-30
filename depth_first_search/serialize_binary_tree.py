from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list

def serialize_tree(root):
    ds = []
    def dfs(node):
        if not node:
            ds.append('x')
            return
        ds.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ds

def deserialize_tree_with_string(s):
    def dfs(nodes):
        val = next(nodes)
        if val == 'x':
            return
        left = dfs(nodes)
        right = dfs(nodes)
        return BTNode(val, left, right)
        
    return dfs(iter(s))

def deserialize_tree_with_nodes(nodes):
    # 如果我们pass nodes as input, 那么nested dfs不需要参数
    def dfs():
        val = next(nodes)
        if val == 'x':
            return
        left = dfs()
        right = dfs()
        return BTNode(val, left, right)
        
    return dfs()


arr_str = "1 2 3 x x 4 x 6 x x 5 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
ret = serialize_tree(bt.root)
print(ret)
# new_bt = deserialize_tree_with_string(ret)
new_bt = deserialize_tree_with_nodes(iter(ret))
pretty_print_bt(new_bt)
