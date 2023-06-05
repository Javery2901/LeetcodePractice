# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque([(root, 0)])
        while queue:
            node, value = queue.popleft()
            if not node.left and not node.right:
                if targetSum == value + node.val:
                    return True
            if node.left:
                queue.append((node.left, value + node.val))
            if node.right:
                queue.append((node.right, value + node.val))
        return False

