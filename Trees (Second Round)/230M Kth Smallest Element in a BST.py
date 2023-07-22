# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        i = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            i += 1
            if i == k:
                return pop_node.val
            cur = pop_node.right

    def kthSmallest_re(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder_re(root):
            if not root:
                return
            inorder_re(root.left)
            if len(res) == k:
                return
            res.append(root.val)
            inorder_re(root.right)
        inorder_re(root)

        return res[-1]
