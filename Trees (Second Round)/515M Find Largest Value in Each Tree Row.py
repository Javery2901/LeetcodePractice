# Definition for a binary tree node.
import collections
from cmath import inf
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            l = len(queue)
            level_max = -inf
            for _ in range(l):
                pop_node = queue.popleft()
                level_max = max(pop_node.val, level_max)
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            res.append(level_max)
        return res

