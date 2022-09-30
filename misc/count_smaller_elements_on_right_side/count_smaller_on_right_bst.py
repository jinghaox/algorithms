# need to create two extra fields
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        # number of times an element has occurred
        self.ele_count = 1

        # denotes the number of nodes on left side
        self.left_count = 0
    
class BST(object):
    def __init__(self, root):
        self.root = root 

    def insert(self, node):
        curr = self.root
        cnt = 0

        # first just count the counts&freqs by traversing the tree
        # then we insert node to the right place
        while curr is not None:
            # the reason we need prev is because we update curr = curr.left/right when counting
            # so we need it to insert the node after counting
            prev = curr
            if node.val > curr.val:
                # if node is larger, then we need all smaller nodes' left counts + current element's count
                cnt += (curr.ele_count + curr.left_count)
                curr = curr.right
            elif node.val < curr.val:
                # if node is smaller, then only need to update the left_count
                curr.left_count += 1
                curr = curr.left
            else:
                # prev = curr
                # prev.ele_count += 1
                # here prev is already curr
                # so we can just do this, no need to use the prvious two lines

                # when equal, we finish traversing, just need to update current node's ele_count
                # then break
                curr.ele_count += 1
                break
        # now to insert the new node
        if prev.val > node.val:
            prev.left = node
        elif prev.val < node.val:
            prev.right = node
        else:
            # when equal, no need to insert node
            # we return the existing cnt + prev's node's left_count
            return cnt + prev.left_count
        return cnt
    
    def print_tree(self, node):
        if node is None:
            return
        self.print_tree(node.left)
        print(f"{node.val}, {node.ele_count}, {node.left_count}", end="->")
        self.print_tree(node.right)

    
def construct_array(nums, n):
    bst = BST(Node(nums[-1]))
    ans = [0]

    for i in range(n-2, -1, -1):
        ans.append(bst.insert(Node(nums[i])))
    bst.print_tree(bst.root)
    return reversed(ans)

nums = [10, 6, 15, 20, 30, 5, 7, 15]
n = len(nums)
ret = construct_array(nums, n)
print(list(ret))

