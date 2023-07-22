# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_it1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


    def preorderTraversal_it2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, False)]
        while stack:
            pop_node, visited = stack.pop()
            if visited:
                res.append(pop_node)
            else:
                if pop_node.right:
                    stack.append((pop_node.right, False))
                if pop_node.left:
                    stack.append((pop_node.left, False))
                stack.append((pop_node, True))
        return res


    def preorderTraversal_re(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if not root:
                return []
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        return res



