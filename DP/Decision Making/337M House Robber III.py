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

    def rob_top_down(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def recursion(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            if root in memo:
                return memo[root]
            # we steal this node
            val1 = root.val
            if root.left:
                val1 += recursion(root.left.left) + recursion(root.left.right)
            if root.right:
                val1 += recursion(root.right.left) + recursion(root.right.right)
            val2 = recursion(root.left) + recursion(root.rgiht)
            memo[root] = max(val1, val2)

            return memo[root]

        return recursion(root)
