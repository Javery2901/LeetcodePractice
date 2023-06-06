# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if left < node.val < right:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            else:
                return False
        return valid(root, -sys.maxsize, sys.maxsize)




