# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees_re(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        node = TreeNode()
        if not root1 and root2:
            node.val = root2.val
            node.left = self.mergeTrees_re(None, root2.left)
            node.right = self.mergeTrees_re(None, root2.right)
        elif root1 and not root2:
            node.val = root1.val
            node.left = self.mergeTrees_re(root1.left, None)
            node.right = self.mergeTrees_re(root1.right, None)
        else:
            node = root1.val + root2.val
            node.left = self.mergeTrees_re(root1.left, root2.left)
            node.right = self.mergeTrees_re(root1.right, root2.right)
        return node

    def mergeTrees_it(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # change roo1
        if not root1:
            return root2
        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()
            if not node2:
                continue
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        return root1


