# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs 同枝上记录一个最大值
        max_value = root.val

        def dfs(root, max_value):
            if not root:
                return 0
            if root.val >= max_value:
                return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
            elif root.val < max_value:
                return dfs(root.left, max_value) + dfs(root.right, max_value)

        return dfs(root, max_value)





