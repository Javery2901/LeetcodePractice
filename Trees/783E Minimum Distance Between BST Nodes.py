# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev_node = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # this is actually inorder traverse
        # use a constant variable to record the former value
        res = [100000]

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev_node:
                res[0] = min(res[0], root.val - self.prev_node.val)
            self.prev_node = root
            inorder(root.right)

        inorder(root)
        return res[0]

    def minDiffInBST_it(self, root: Optional[TreeNode]) -> int:
        prev_value = None
        res = inf
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur.left)
                cur = cur.left
            pop_node = stack.pop()
            if prev_value:
                res = min(res, pop_node.val - prev_value)
            prev_value = pop_node.val
            cur = cur.right
        return res
