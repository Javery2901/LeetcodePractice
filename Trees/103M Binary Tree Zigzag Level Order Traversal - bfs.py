# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        i = -1
        res = []
        queue = collections.deque([root])
        while queue:
            i += 1
            ls = []
            for _ in range(len(queue)):
                node, level = queue.popleft()
                ls.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if i % 2 != 0:
                ls.reverse()
            res.append(ls)
        return res
