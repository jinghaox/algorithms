from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list

def lca_on_bst(root, p, q):
    cur_val = root.val
    if p <= cur_val and q <= cur_val:
        if p == cur_val or q == cur_val:
            return root
        else:
            return lca_on_bst(root.left, p, q)

    if p >= cur_val and q >= cur_val:
        if p == cur_val or q == cur_val:
            return root
        else:
            return lca_on_bst(root.right, p, q)
    
    if p >= cur_val and q <= cur_val or p <= cur_val and q >= cur_val:
        return root
    
    # return root


arr_str = "6 2 0 x x 4 3 x x 5 x x 8 7 x x 9 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
# pretty_print_bt(bt.root)
p = 0
q = 5
node = lca_on_bst(bt.root, p, q)
print(node.val)