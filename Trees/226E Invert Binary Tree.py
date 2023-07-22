# Definition for a binary tree node.
import collections
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
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                node.left, node.right = node.right, node.left
        return root

    def invertTree_stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        stack = [root]
        while stack:
            pop_node = stack.pop()
            pop_node.left, pop_node.right = pop_node.right, pop_node.left
            if pop_node.right:
                stack.append(pop_node.right)
            if pop_node.left:
                stack.append(pop_node.left)
        return root

    def invertTree_re(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree_re(root.left)
        self.invertTree_re(root.right)
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





