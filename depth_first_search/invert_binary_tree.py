from pretty_print_bt import BT, BTNode, print_bt, pretty_print_bt, generate_tree_list

def invert_binary_tree(root):
    if root is None:
        return
    
    # can't do root.left = invert_binary_tree(root.right)
    # then root.right = invert_binary_tree(root.left)
    # 因为这时root.left已经反转过了
    # 所以需要临时变量两个
    # left = invert_binary_tree(root.right)
    # right = invert_binary_tree(root.left)
    # root.left = left 
    # root.right = right 

    # 一个临时变量的方法
    left = invert_binary_tree(root.right)
    root.right = invert_binary_tree(root.left)
    root.left = left 
    return root 

def invert_binary_tree_algo(root):
    # algomonster的算法是建一个新节点
    if root is None:
        return None
    return BTNode(root.val, invert_binary_tree(root.right), invert_binary_tree(root.left))

    

arr_str = "8 5 2 x 3 x x 6 x x 10 x 14 x x"
arr = generate_tree_list(arr_str)
bt = BT()
bt.build_tree(iter(arr), int)
pretty_print_bt(bt.root)
bt1 = invert_binary_tree_algo(bt.root)
pretty_print_bt(bt1)
