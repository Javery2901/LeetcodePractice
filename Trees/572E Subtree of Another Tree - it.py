# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(root, subroot):  # dfs
            if root and subroot:
                return root.val == subroot.val and same_tree(root.left, subroot.left) and \
                    same_tree(root.right, subroot.right)
            return root == subroot

        stack = [root]
        while stack:
            node = stack.pop()
            if same_tree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
