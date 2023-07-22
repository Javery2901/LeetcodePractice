# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                # if some subtree has already been unbalanced, return -1
                return -1
            return 1 + max(left_height, right_height)
        return height(root) != -1


node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(3)
node.left.left.left = TreeNode(4)
node.right = TreeNode(2)
node.right.right = TreeNode(3)
node.right.right.right = TreeNode(4)
s = Solution()
s.isBalanced(node)