from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list, find_target_node

def lca(root, node1, node2):
    def dfs(root, node):
        if not root:
            return None
        if root == node:
            return [root.val]
        left = dfs(root.left, node)
        right = dfs(root.right, node)
        if left:
            left.append(root.val)
            return left
        if right:
            right.append(root.val)
            return right

    stk1 = dfs(root, node1)
    if stk1 is not None:
        stk1 = stk1[::-1]  
    stk2 = dfs(root, node2)
    if stk2 is not None:
        stk2 = stk2[::-1]

    if not stk1 or not stk2:
        return None

    i = 0
    common_ancestor = None
    while i < min(len(stk1), len(stk2)):
        if stk1[i] == stk2[i]:
            common_ancestor = stk1[i]
            i += 1
        else:
            break
    return common_ancestor

def lca_algo(root, node1, node2):
    if not root:
        return

    # case 2 
    if root == node1 or root == node2:
        return root

    left = lca_algo(root.left, node1, node2)
    right = lca_algo(root.right, node1, node2)

    # case 3a both return non-null node
    if left and right:
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 3b and 3c, report target node or LCA back to parent
    # here is case 3c
    if left:
        return left
    if right:
        return right

    # after case 3c, now it's case 3b, not found return null
    return None


arr_str = "6 2 0 x x 4 3 x x 5 x x 8 7 x x 9 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
node1 = find_target_node(bt.root, 0)
node2 = find_target_node(bt.root, 5)
node_c = lca(bt.root, node1, node2)
# node_c = lca_algo(bt.root, node1, node2)
print(node_c)