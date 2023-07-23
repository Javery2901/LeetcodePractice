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
        self.max_depth = -inf
        self.leftmost_value = None

    def findBottomLeftValue_re(self, root: Optional[TreeNode]) -> int:

        def recursive(root, depth):
            if not root.left and not root.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.leftmost_value= root.val
                return

            if root.left:
                recursive(root.left, depth + 1)
            if root.right:
                recursive(root.right, depth + 1)

        recursive(root, 0)
        return self.leftmost_value

    def findBottomLeftValue_it(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -inf

        stack = [(root, 0)]
        res = None
        while stack:
            pop_node, depth = stack.pop()
            if depth > self.max_depth:
                self.max_depth = depth
                res = pop_node.val
            if pop_node.right:  # FILO stack
                stack.append((pop_node.right, depth + 1))
            if pop_node.left:
                stack.append((pop_node.left, depth + 1))
        return res



