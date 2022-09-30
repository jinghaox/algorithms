def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root

    # # return non-null return value from the recursive calls
    # left = dfs(root.left, target)

    # if left is not None:
    #     return left

    # # at this point, we know left is null, and right could be null or non-null
    # # we return right child's recursive call result directly because
    # # - if it's non-null we should return it
    # # - if it's null, then both left and right are null, we want to return null
    # return dfs(root.right, target)
    # # the code can be shortened to: return dfs(root.left, target) or dfs(root.right, target)
    return dfs(root.left, target) or dfs(root.right, target)
