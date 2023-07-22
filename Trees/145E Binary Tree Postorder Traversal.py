# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal_it1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.reverse()
        return res

    def postorderTraversal_it2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, False)]
        while stack:
            pop_node, visited = stack.pop()
            if visited:
                res.append(pop_node.val)
            else:
                stack.append((pop_node, True))
                if pop_node.right:
                    stack.append((pop_node.right, False))
                if pop_node.left:
                    stack.append((pop_node.left, False))
        return res

    def postorderTraversal_it3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root] * 2
        while stack:
            pop_node = stack.pop()
            if stack and pop_node == stack[-1]:
                if pop_node.right:
                    stack.append(pop_node.right)
                    stack.append(pop_node.right)
                if pop_node.left:
                    stack.append(pop_node.left)
                    stack.append(pop_node.left)
            else:
                res.append(pop_node.val)
        return res

    def postorderTraversal_re(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

