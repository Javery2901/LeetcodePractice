# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(root):
            if not root:
                return 0
            left_sum = path_sum(root.left)
            right_sum = path_sum(root.right)
            self.max_path = max(self.max_path, root.val, root.val + left_sum, root.val + right_sum, left_sum + right_sum + root.val)
            return max(left_sum + root.val, right_sum + root.val, root.val)

        self.max_path = root.val
        path_sum(root)
        return int(self.max_path)
