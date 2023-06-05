# Definition for a binary tree node.
import collections
from typing import List, Optional
"""
O(n), using memo to save the index
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        memo = {}
        for k, v in enumerate(inorder):
            memo[v] = k
        preorder_deque = collections.deque(preorder)

        def build(left, right):
            if left >= right:
                return
            root_val = preorder_deque.popleft()
            root = TreeNode(root_val)
            index = memo[root_val]
            root.left = build(left, index)
            root.right = build(index + 1, right)
            return root
        return build(0, len(inorder))
