# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # create a dp tree, each node has two value:
        # (rob this node and ignore children's value, ignore this node and rob the biggest value of children)

        def dfs(node):
            if not node:
                return 0, 0
                # the leaf
            left = dfs(node.left)  # left = (0, 0)
            right = dfs(node.right)  # right = (0, 0)
            return node.value + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])

        return max(dfs(root))
