# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves_re(self, root: Optional[TreeNode]) -> int:

        def recursive(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            left_value = 0
            if root.left:
                if not root.left.left and not root.left.right:
                    left_value = root.left.val
            return left_value + recursive(root.left) + recursive(root.right)

        return recursive(root)

    def sumOfLeftLeaves_it(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        st = [root]
        result = 0
        while st:
            node = st.pop()
            if node.left and node.left.left is None and node.left.right is None:
                result += node.left.val
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return result
