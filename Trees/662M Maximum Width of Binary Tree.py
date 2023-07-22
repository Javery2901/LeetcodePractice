# Definition for a binary tree node.
import collections
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Hint: If parents index is n left child is 2n and right child is 2n+1
        # we need to give every node a index, and maintain a constant variable for the largest distance every layer
        # use bfs
        max_width = 1
        queue = collections.deque([(root, 1)])
        while queue:
            l = len(queue)
            left = inf
            right = -inf
            for _ in range(l):
                pop_node, index = queue.popleft()
                left = min(left, index)
                right = max(right, index)
                if pop_node.left:
                    queue.append((pop_node.left, index * 2))
                if pop_node.right:
                    queue.append((pop_node.right, index * 2 + 1))
                max_width = max((right - left) + 1, max_width)
        return max_width