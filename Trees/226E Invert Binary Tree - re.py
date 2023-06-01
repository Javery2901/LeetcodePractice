# Definition for a binary tree node.
from typing import Optional
from binarytree import Node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


s = Solution()
qroot = TreeNode(4)
qroot.left = TreeNode(2)
qroot.left.left = TreeNode(1)
qroot.left.right = TreeNode(3)
qroot.right = TreeNode(7)
qroot.right.left = TreeNode(6)
qroot.right.right = TreeNode(9)
goal_root = s.invertTree(qroot)
# while goal_root:
#     print(goal_root.val)
#     goal_root = goal_root.left





