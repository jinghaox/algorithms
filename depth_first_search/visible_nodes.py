from pretty_print_bt import BT, print_bt
def visible_nodes(root):
    def dfs(node, max_sofar):
        if not node:
            return 0
        total = 0

        if node.val >= max_sofar:
            total += 1
            max_sofar = node.val
        total += dfs(node.left, max_sofar)
        total += dfs(node.right, max_sofar)
        return total
    
    return dfs(root, -float('inf'))

def visible_nodes_alternate(root):
    def dfs(node, max_sofar):
        if not node:
            return 0
        # print(f'cur_node = {node.val}, with max_sofar = {max_sofar}')
        if node.val >= max_sofar:
            print(f'visible node = {node.val}')
            return 1+ dfs(node.left, node.val) + dfs(node.right, node.val)
        else:
            return dfs(node.left, max_sofar) + dfs(node.right, max_sofar)
    
    return dfs(root, -float('inf'))

# arr = [6,4,3,'x','x',5,'x','x',8,'x','x']
arr = [5, 7, 3, 'x', 'x', 8, 'x', 'x', 6, 'x', 'x']
bt = BT()
bt.build_tree(iter(arr), int)
# print_bt(bt.root)
ret = visible_nodes_alternate(bt.root)
print(ret)
