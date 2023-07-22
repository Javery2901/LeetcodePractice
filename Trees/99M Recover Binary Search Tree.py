# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder
        res = []

        def inorder_re(root):
            if not root:
                return
            inorder_re(root.left)
            res.append(root)
            inorder_re(root.right)

        inorder_re(root)
        first, second = None, None
        for i in range(1, len(res)):
            if res[i - 1].val > res[i].val:
                first = res[i - 1]
                break
        for i in range(len(res) - 1, 0, -1):
            if res[i - 1].val > res[i].val:
                second = res[i]
                break
        first.val, second.val = second.val, first.val



