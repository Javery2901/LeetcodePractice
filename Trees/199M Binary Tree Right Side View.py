# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            length = len(queue)
            for i in range(length):
                pop_node = queue.popleft()
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
                if i == length-1:
                    res.append(pop_node.val)
        return res

