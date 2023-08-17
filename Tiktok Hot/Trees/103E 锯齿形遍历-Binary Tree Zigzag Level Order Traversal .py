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
        res = []
        if not root:
            return res
        layer = 0
        queue = collections.deque([root])
        while queue:
            temp = []
            for _ in range(len(queue)):
                pop_node = queue.popleft()
                temp.append(pop_node.val)
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            if layer % 2 == 1:
                temp.reverse()
            layer += 1
            res.append(temp)
        return res


