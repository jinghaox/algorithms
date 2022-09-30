class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def build_tree(nodes, f):
    # this one is not similar to Binary Tree
    # because for a leaf node, we don't add None as its children
    # but in Binary tree, left/right child may be None
    # 但是最后都是要return 一个新的Node
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

def build_tree_pop(nodes, f):
    val = nodes.pop(0)
    num = int(nodes.pop(0))
    children = [build_tree_pop(nodes, f) for _ in range(num)]
    return Node(f(val), children)

def print_tree(root):
    if root is None:
        print("\n")
        return
    print(root.val, end=" ")
    for c in root.children:
        print_tree(c)



def find_all_paths_not_working(root):
    # find all root-leaf path
    # previously it's not working
    # now it works
    def dfs(root, path, res):
        # how to exit??? this one seems not working, why?
        # when we enter into dfs as dfs(5, path), 5 itself is not None
        # but 5's children all all None, it means it's a leaf node
        # so we should stop and print the path now
        if root is None:
            return
        if root.children == []:
            res.append(path + [root.val])
            return
        # path.append(root.val)
        for c in root.children:
            # if c is not None:
            #     # dfs(c, path + [str(root.val)])
            #     # path.append() returns None
            #     # path = path.append(), where the new path is still None
            #     # to overcome this, we need to use path + [a], which actually creates a new list (without a name)
            #     # or update path first, then pass "path" to the function, in this way, need to pop()
            #     path.append(root.val)
            #     dfs(c, path)
            #     path.pop()

            # if we don't check if c is not None here, then we need to add 
            # if root is None: return as an exit of the recursion
            path.append(root.val)
            dfs(c, path, res)
            path.pop()
    path = []
    res = []
    dfs(root, path, res)
    return res

def find_all_paths(root):
    # dfs helper function
    def dfs(root, path, res):
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        # dfs on each non-null child
        for child in root.children:
            if child is not None:
                dfs(child, path + [str(root.val)], res)
                # this path+[] is tricky, the new arg path+[] is passed in, but after 
                # the dfs call, the path is still the orignial path
                # this path +[] is also non-efficient, it creates a new list every time
                # so to improve this, use append & pop

                # if we update path here, then we need to pop
                # path = path + [str(root.val)]
                # dfs(child, path, res)
                # path.pop()

    res = []
    if root: dfs(root, [], res)
    print(res)
    return res

def ternary_tree_paths(root):
    # this is my final version
    # dfs helper function
    def dfs(root, path, res):
        if root is None:
            return
        if root.children == []:
            res.append('->'.join(path) + '->' + str(root.val))
            return
        # dfs on all children, including None
        for child in root.children:
            dfs(child, path + [str(root.val)], res)

    res = []
    if root: dfs(root, [], res)
    return res
# ----------------------------------------------------------------
def build_tree_with_x(nodes, f):
    val = nodes.pop(0)
    if val == 'x':
        return None
    children = []
    for _ in range(3):
        children.append(build_tree_with_x(nodes, f))
    return Node(f(val), children)

def print_tree_with_x(root):
    if root is None:
        print("x", end=" ")
        return
    print(root.val, end=" ")
    for c in root.children:
        print_tree_with_x(c)

def find_all_paths_with_x(root):
    def dfs(root, path, res):
        if root is None:
            return
        if root.children == [None, None, None]:
            # when a node's children are all None, it means it's a leaf node
            res.append(path + [root.val])   # to save the results, not print, we need another arg res
            return
        path.append(root.val)
        for c in root.children:
            # na matter c is None or not, always call dfs
            # if it's None, in next recursion, it will just return
            dfs(c, path, res)
        # here we need to pop !!!
        path.pop()

    path = []
    res = []
    dfs(root, path, res)
    print(res)

arr = [1,3,2,1,5,0,3,0,4,0]
#           1
#        2  3  4
#     5
tt = build_tree(iter(arr), int)
# tt = build_tree_pop(arr, int)
print_tree(tt)
print("\n")
ret = find_all_paths_not_working(tt)
print(ret)

# arr = [1,2,5,'x','x','x','x','x',3,'x','x','x',4,'x','x','x']
# tt = build_tree_with_x(arr, int)
# print_tree_with_x(tt)
# print("\n")
# find_all_paths_with_x(tt)
