class BTNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class BT():
    def __init__(self):
        self.root = None

    def build_tree(self, nodes, f):
        def dfs(nodes, f):
            # this uses iterator and generator
            # nodes can't be a list, must use iter(list)
            val = next(nodes)
            if val == 'x':
                return None
            left = dfs(nodes, f)
            right = dfs(nodes, f)
            return BTNode(f(val), left, right)

        def dfs2(nodes, ix, f):
            # my version, without using iterator and generator
            # using the index
            # but, the index can't be a scalar, needs to be a list, so it can be shared
            # otherwise, after left=dfs2() returns, it go to right=dfs2(), it will use the previous ix in the stack
            # but if we use ix=[], then it will use the current ix
            if ix[0] > len(nodes)-1:
                return None
            val = nodes[ix[0]]
            # every time, after we get the current index's value, we increase the ix by one
            ix[0] += 1
            if val == 'x':
                return None
            left = dfs2(nodes, ix, f)
            right = dfs2(nodes, ix, f)
            return BTNode(f(val), left, right)

        def bfs(nodes, ix, f):
            # for bfs, have to use a queue, check it later
            pass
        self.root = dfs(nodes, f)
        # self.root = dfs2(nodes, [0], f)

    def create_bt(self, arr):
        node0 = BTNode(val=arr[0])
        node1 = BTNode(val=arr[1])
        node2 = BTNode(val=arr[2])
        node3 = BTNode(val=arr[3])
        node4 = BTNode(val=arr[4])
        node5 = BTNode(val=arr[5])
        node6 = BTNode(val=arr[6])

        self.root = node0
        self.root.left = node1
        self.root.right= node2
        self.root.left.left = node3
        self.root.left.right = node4
        self.root.right.left = node5
        self.root.right.right = node6
    
def print_bt(root): # in - order
    # if root.left is not None:
    #     print_bt(root.left)
    # print(f"{root.val}-", end="")
    # if root.right is not None:
    #     print_bt(root.right)

    # this is better, no need to check .left/right since 
    # the recursive call will check root is None or not
    if root is None:
        return
    print_bt(root.left)
    print(f"{root.val}-", end="")
    print_bt(root.right)


def pretty_print_bt(root):
    # In-order

    indent_per_level = '\t'
    def dfs(root, indent_level):
        if root is None:
            return ''
        curr_indent_level = indent_level + indent_per_level
        dfs(root.left, curr_indent_level)
        print(curr_indent_level + str(root.val))
        dfs(root.right, curr_indent_level)

    dfs(root, '')

def real_pretty_print(root):
    # dfs can't do it, it's still the same as pretty_print, I think we need bfs
    indent_per_level = '\t'
    format_dict = {}
    def dfs(root, indent_level):
        if root is None:
            return ''
        curr_indent_level = indent_level + indent_per_level
        dfs(root.left, curr_indent_level)
        format_dict[root.val] = curr_indent_level
        dfs(root.right, curr_indent_level)


    def in_order_dfs(root):
        if root is None:
            return
        in_order_dfs(root.left)
        print(f"{format_dict[root.val]} {root.val}")
        in_order_dfs(root.right)

    dfs(root, '')
    print(format_dict)
    in_order_dfs(root)

def generate_tree_list(arr_str):
    arr = []
    for x in arr_str.split():
        if x == 'x':
            arr.append('x')
        else:
            arr.append(x)
    print(f'generate list = {arr}')
    return arr


def find_target_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root

    # left = find_target_node(root.left, target)
    # if left is not None:
    #     return left
    # right = find_target_node(root.right, target)

    # # this actually can be shorten to "return right"

    # # if right is not None:
    # #     return right 
    # # else:
    # #     return None
    # return right

    # furthermore, the left&right block can be shorten to this

    return find_target_node(root.left, target) or\
           find_target_node(root.right, target)

def tree_max_depth(root):
    if root is None:
        return 0

    max_depth = max(tree_max_depth(root.left), tree_max_depth(root.right)) + 1
    return max_depth

def visible_tree_node_mine(root):

    visible = 0
    def dfs(root, max_val):
        # since we need to pass the value down from parent to children, so need
        # to pass it as a state in the argument list
        nonlocal visible
        if root is None:
            return

        if root.val > max_val:
            # I used dfs(root, root.val), so for the first node, I must use >= here
            # otherwise, it won't be counted
            # however, then for other nodes, it also means >=, so it doesn't conform to the problem
            # i.e. visible nodes are great than the max number from the root (not greater than and equal to)
            # so the solution is, we need to call dfs(root, -inf)
            visible += 1
            max_val = root.val
            print(f'{root.val}', end = " ")

        dfs(root.left, max_val)
        dfs(root.right, max_val)

    dfs(root, float('-inf'))
    return visible

def visible_tree_node(root):
    # algomonster is using return value, not global value
    def dfs(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val > max_sofar:
            max_sofar = root.val
            total += 1

        # total += dfs(root.left, max(max_sofar, root.val))
        # # max_sofar for child node is the larger of previous max and current node val
        # total += dfs(root.right, max(max_sofar, root.val))

        total += dfs(root.left, max_sofar) # root.left will return it's num of visible node, so the total is +=
        total += dfs(root.right, max_sofar)

        return total

    # start max_sofar with smallest number possible so any value root has is smaller than it
    return dfs(root, -float('inf'))

def is_balanced(root):
    def dfs(root):
        # we want dfs to return the height, so we can compare the height of left and right
        # if we return true/false, is it possible?
        # No, because for a node, if left is True, right is True, doesn't mean this node will return True
        if root is None:
            # this means we return the height, not return False/True
            return 0
        left_height = dfs(root.left)  # this can be called, since if root.left is None, then return 0, otherwise, return it's height
        right_height = dfs(root.right)
        if left_height == -1 or right_height == -1:
            # if any subtree is imbalanced, then the tree from this node is also imbalanced
            # we can return -1 directly
            return -1
        if abs(left_height - right_height) <= 1:
            return max(left_height, right_height) + 1
        else:
            return -1
    
    return dfs(root) != -1

def invert_bt(root):
    def dfs(root):
        if root is None:
            return None
        right = dfs(root.left)
        left = dfs(root.right)
        return BTNode(root.val, left, right)
    return dfs(root)


def serialize(root):
    ds = []
    # no need to pass ds into dfs function as an argument
    def dfs(root):
        if root is None:
            ds.append('x')
            # we need return here
            return
        ds.append(root.val)
        dfs(root.left)
        dfs(root.right)
    
    dfs(root)
    return ds

def deserialize(arr):
    def dfs(arr):
        # shall return a node, not a value
        # if is 'x', return None as a node
        # because left can be None, right can also be None, so None is a valid node
        val = arr.pop(0)
        if val == 'x':
            return None
        left_node = dfs(arr)
        right_node = dfs(arr)
        return BTNode(val, left_node, right_node)
    return dfs(arr)

def print_tree(root):
    if not root:
        yield "x"
        return
    yield str(root.val)
    # need to use yield from for generator, not return
    yield from print_tree(root.left)
    yield from print_tree(root.right)

def find_node(root, target):
    # find the node with val==target, and return the node, not the value
    if not root:
        return
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)

def lca(root, node1, node2):
    # lowest common ancestor
    def dfs(root, node):
        if not root:
            return None
        if root == node:
            res = [root.val]
            return res
        # for current node root, if the return of its left or right is not None, 
        # means it has the target, then we need to add root to the stack as well
        # if we don't use returned value, but just use a stack, 
        # it's not possible to determine if the current node should be added to the stack or not
        # because for a non-ancestor node, the res stack also has the target node already
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
    # return of dfs() is [target, ancestor...], so we need to reverse it to find the common ancestor
    stk2 = dfs(root, node2)
    if stk2 is not None:
        stk2 = stk2[::-1]
    print(stk1)
    print(stk2)

    if not stk1 or not stk2:
        return None

    common_ancestor = None
    i = 0
    while i < min(len(stk1), len(stk2)):
        if stk1[i] == stk2[i]:
            # for [6,4], [6], first set 6 to common_ancestor
            # then even we exit the loop, we still have common_ancestor
            common_ancestor = stk1[i]
            i += 1
        else:
            break
    return common_ancestor

def delete_nodes_to_forest(root, remov_list):
    def dfs(root, res):
        if root is None:
            return None
        root.left = dfs(root.left, res)
        root.right = dfs(root.right, res)

        if root.val not in remov_list:
            return root
        if root.left:
            res.append(root.left)
        if root.right:
            res.append(root.right)
        return None
    res = []
    d_ret = dfs(root, res)
    if d_ret is not None:
        res.append(d_ret)

    ret = []
    for x in res:
        ret.append(x.val)
    return ret


if __name__ == '__main__':
    bt = BT()
    # bt.create_bt([1,2,3,4,5,6,7])
    # pretty_print_bt(bt.root)
    # setattr(bt, 'val', '12')
    # print(getattr(bt, 'val'))

    # ret = find_target_node(bt.root, 5)
    # print(ret.val)

    # ret = tree_max_depth(bt.root)
    # print(ret)

    # bt.create_bt([4,2,3,1,5,6,7])
    # bt.create_bt([5,8,3,1,2,8,6])

    # arr = [5,8,3,'x','x',8,'x','x',6,'x','x']
    # arr = [5,4,3,'x','x',8,'x','x',6,'x','x']
    # # this is dfs created 
    # # so it's like
    # #             5
    # #      8
    # #    3
    # #  x   x
    # #         8
    # #       x   x
    # #                    6
    # # bt.build_tree(iter(arr), int)
    # bt.build_tree(arr, int)

    # # print_bt(bt.root)
    # pretty_print_bt(bt.root)
    # ret = visible_tree_node_mine(bt.root)
    # # ret = visible_tree_node(bt.root)
    # print("\nhas {ret} visible nodes")

    # arr = [5,4,3,'x','x',8,'x','x',6,'x', 7, 2, 'x','x', 'x']
    # bt.build_tree(arr, int)
    # pretty_print_bt(bt.root)
    # ret = is_balanced(bt.root)
    # print(ret)

    # ret = serialize(bt.root)
    # print(ret)
    # new_root = deserialize(ret)
    # ret = serialize(new_root)
    # print(ret)

    # print(list(print_tree(new_root)))

    arr = [6,4,3,'x','x',5,'x','x',8,'x','x']
    # arr = ['x']
    bt.build_tree(iter(arr), int)
    # pretty_print_bt(bt.root)
    ret = delete_nodes_to_forest(bt.root, [5])
    print(ret)

    # node1 = find_node(bt.root, 3)
    # node2 = find_node(bt.root, 5)
    # ans = lca(bt.root, node1, node2)
    # print(ans)
    # 
    # new_bt = invert_bt(bt.root)
    # pretty_print_bt(new_bt)
