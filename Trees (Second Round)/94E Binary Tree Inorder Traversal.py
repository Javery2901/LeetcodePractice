# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_it1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            pop_node = stack.pop()
            res.append(pop_node.val)
            cur = pop_node.right
        return res

    def inorderTraversal_it2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, False)]
        while stack:
            pop_node, visited = stack.pop()
            if visited:
                res.append(pop_node.val)
            else:
                if pop_node.left:
                    stack.append((pop_node.left, False))
                stack.append((pop_node, True))
                if pop_node.right:
                    stack.append((pop_node.right, False))
        return res


    def inorderTraversal_re(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
