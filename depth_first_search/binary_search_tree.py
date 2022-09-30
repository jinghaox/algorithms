class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left 
        self.right = right 


class BST():
    def __init__(self):
        self.root = None

    def build_tree(self, arr):
        # if using generator&iterator, see depth_first_search/pretty_print_bt.py
        def dfs(arr):
            val = arr.pop(0)
            if val == 'x':
                return None
            left = dfs(arr)
            right = dfs(arr)
            return Node(val, left, right)
        self.root = dfs(arr)
    

    def print_tree(self):
        def dfs(root):
            if root is None:
                print('x', end=" ")
                # don't forget this return, because we need this for recursion
                # call
                return
            # no need to check if root.left is None or not, since in next
            # recursion, if root is None is checked
            dfs(root.left)
            print(root.val, end=" ")
            dfs(root.right)

        dfs(self.root)

    def validate_bst(self):
        def dfs(root, min_val, max_val):
            if root is None:
                return True

            # why return True directly not working here?
            # because when it's good, it doesn't mean we can return True
            # immediately, we need to check left/right further

            if root.val >= min_val and root.val <= max_val:
                # Note: for left, we pass root.val as max_val
                # otherwise, we need to update the max_val, but how?
                return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
                # return True
            else:
                return False

            # if root.val < min_val or root.val > max_val:
            #     return False
            # return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

            # if not (min_val <= root.val <= max_val):
            #     return False
            # return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        return dfs(self.root, float('-inf'), float('inf'))
    
    def insert_node_iterate(self, val):
        # non-recursive version
        curr = self.root
        if curr is None:
            self.root = Node(val, None, None) 
        parent = None
        while curr is not None:
            parent = curr
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                break
        if val < parent.val:
            parent.left = Node(val, None, None)
        elif val > parent.val:
            parent.right = Node(val, None, None)
    
    def insert_node(self, val):
        def dfs(root, val):
            if root is None:
                return Node(val, None, None)
            if root.val > val:
                # can't return here directly, need to update the tree
                # 这里，我们update root.left by dfs(root.left, val), 因为我们要把val插入到root.left中去
                root.left = dfs(root.left, val)
            if root.val < val:
                root.right = dfs(root.right, val)
            return root
        return dfs(self.root, val)

def test(a, b):
    # this is the same as the last line
    # if not a:
    #     return False
    # # here a is True 
    # if not b:
    #     return False 
    # return True
    return a and b
def find_closest_value(root, target):
    # works, but weird...to use closest_node in arg and return
    def search(root, closest_node):
        if not root:
            return closest_node

        if not closest_node or abs(root.val - target) < abs(closest_node.val - target):
            closest_node = root

        if root.val < target:
            return search(root.right, closest_node)
        elif root.val > target:
            return search(root.left, closest_node)
        return closest_node

    closest_node = search(root, None)
    return closest_node.val

def find_closest_value_iterative(root, target):

    diff = float('inf')
    closest = None
    while root:

        if root.val == target:
            return root

        cur_diff = abs(root.val - target)
        if cur_diff < diff:
            diff = cur_diff
            closest = root

        if root.val < target:
            root = root.right
        else:
            root = root.left
    return closest.val

def find_closest_value_recur(root, target):
    diff = float('inf')
    closest = [None]

    def search(root, diff, closest):
        # nonlocal diff
        # nonlocal closest
        # either use [None], or use nonlocal
        # no need to return closest
        if not root:
            return

        cur_diff = abs(root.val - target)
        if cur_diff < diff:
            diff = cur_diff
            closest[0] = root

        if root.val < target:
            search(root.right, diff, closest)
        else:
            search(root.left, diff, closest)
    search(root, diff, closest)
    return closest[0].val

class Solution:
    def closestValue(self, root, target):
        self.closest = None

        self.search(root, target)

        return self.closest.val

    def search(self, root, target):
        if not root:
            return

        if not self.closest or abs(root.val - target) < abs(self.closest.val - target):
            self.closest = root

        if target < root.val:
            self.search(root.left, target)
        elif target > root.val:
            self.search(root.right, target)


def get_range_sum(root, low, high):
    # leet code 938
    def get_sums(root, sums):
        if not root:
            return 0

        if root.val < low:
            get_sums(root.right, sums)
        elif root.val > high:
            get_sums(root.left, sums)
        elif low <= root.val <= high:
            get_sums(root.left, sums) 
            get_sums(root.right, sums)
            sums[0] += root.val
    sums = [0]
    get_sums(root, sums)
    return sums

def get_range_sum_new(root, low, high):
    sums = [0]
    def get_sum(root, sums):
        if not root:
            return
        if low<= root.val <= high:
            sums[0] += root.val
        if low < root.val:
            get_sum(root.left, sums)
        if high > root.val:
            get_sum(root.right, sums)
    get_sum(root, sums)
    return sums

bst = BST()
bst.build_tree([6, 4, 3, 'x', 'x', 5, 'x', 'x', 8, 'x' ,'x'])
# ret = bst.validate_bst()
# print(ret)
# 
# bst.insert_node(7)
# bst.print_tree()

# sl = Solution()
# ret = sl.closestValue(bst.root, 4)
# ret = find_closest_value(bst.root, 4.51)
# ret = find_closest_value_iterative(bst.root, 4.51)

# ret = find_closest_value_recur(bst.root, 4)
# print(ret


# test_case_a =[True, True, False, False]
# test_case_b =[True, False, True, False]
# for i in range(len(test_case_a)):
#     a = test_case_a[i]
#     b = test_case_b[i]
#     print(test(a, b))

ret = get_range_sum(bst.root, 5, 7)
print(ret)

