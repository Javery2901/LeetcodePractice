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
        dic = {}
        for i, n in enumerate(inorder):
            dic[n] = i
        # postorder: the last one is root

        def build(left, right):
            if left >= right:
                return
            value = postorder.pop()
            node = TreeNode(value)
            index = dic[value]  # index = 1, 1 之前的均为left，之后的均为right
            node.right = build(index + 1, right)
            node.left = build(left, index)
            return node

        return build(0, len(inorder))