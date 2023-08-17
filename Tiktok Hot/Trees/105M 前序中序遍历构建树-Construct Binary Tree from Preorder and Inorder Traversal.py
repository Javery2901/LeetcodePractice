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
        # inorder, 确定的是他的index，index之前的均为left， 之后的均为right
        # preorder pop出来的军可看作是root，所以每次会将inorder断开
        dic = {}
        for i, n in enumerate(inorder):
            dic[n] = i  # {9: 0, 3:1, 15:2, 20:3, 7:4}
        queue = collections.deque(preorder)

        def build(left, right):
            if left > right:
                return
            value = queue.popleft()
            node = TreeNode(value)
            index = dic[value]  # partition the left part and right part
            node.left = build(left, index)
            node.right = build(index + 1, right)
            return node

        return build(0, len(inorder))