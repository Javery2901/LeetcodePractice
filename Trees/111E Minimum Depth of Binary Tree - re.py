# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left and root.right):
            if not (root.left or root.right):
                return 1
            else:
                if not root.left:
                    return self.minDepth(root.right) + 1
                else:
                    return self.minDepth(root.left) + 1
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            return min(left_depth, right_depth) + 1