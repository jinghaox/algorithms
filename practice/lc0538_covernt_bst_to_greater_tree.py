# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root):
        # cur_sum = 0
        # def helper(node):
        #     nonlocal cur_sum
        #     if node is None:
        #         return
        #     helper(node.right)
        #     temp = node.val
        #     node.val += cur_sum
        #     cur_sum += temp
        #     helper(node.left)
        # helper(root)

        # if we don't use nonlocal cur_sum, we can pass it as an argument
        # so for each call, cur_sum is updated, and we need to return cur_sum
        def dfs(node, cur_sum):
            if node is None:
                return cur_sum 
            cur_sum = dfs(node.right, cur_sum)
            temp = node.val
            node.val += cur_sum
            cur_sum += temp
            cur_sum = dfs(node.left, cur_sum)
            return cur_sum
        
        dfs(root, 0)
        return root