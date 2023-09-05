# Definition for a binary tree node.
from cmath import inf
from typing import Optional
# 543# 找树的直径类型相同
"""
A path in a binary tree is a sequence of nodes 
where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = -inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(root):
            if not root:
                return 0
            left_sum = path_sum(root.left)
            right_sum = path_sum(root.right)
            self.max_path = max(self.max_path, root.val, root.val + left_sum, root.val + right_sum, left_sum + right_sum + root.val)
            return max(left_sum + root.val, right_sum + root.val, root.val)

        path_sum(root)
        return self.max_path
