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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        memo = {}
        for k, v in enumerate(inorder):
            memo[v] = k

        def tree(left, right):
            if left >= right:
                return
            node_val = postorder.pop()
            node = TreeNode(node_val)
            node_index = memo[node_val]
            node.right = tree(node_index, right)
            node.left = tree(left, node_index + 1)
            return node

        return tree(0, len(inorder))

