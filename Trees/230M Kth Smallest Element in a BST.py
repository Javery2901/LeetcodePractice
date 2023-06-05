# Definition for a binary tree node.
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
