# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree_re(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subtree_check(root, subroot):
            if not root and not subroot:
                return True
            if (not root and subRoot) or (root and not subroot):
                return False
            if root.val == subroot.val:
                return subtree_check(root.left, subroot.left) and subtree_check(root.right, subroot.right)
            else:
                return False

        def start_node(root, subroot):
            if not root:
                return False
            if root.val == subroot.val:
                if subtree_check(root, subroot):
                    return True
            return start_node(root.left, subroot) or start_node(root.right, subroot)

        return start_node(root, subRoot)

    def isSubtree_it(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subtree_check(root, subroot):
            if not root and not subroot:
                return True
            if (not root and subRoot) or (root and not subroot):
                return False
            if root.val == subroot.val:
                return subtree_check(root.left, subroot.left) and subtree_check(root.right, subroot.right)
            else:
                return False

        stack = [root]
        while stack:
            node = stack.pop()
            if subtree_check(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
