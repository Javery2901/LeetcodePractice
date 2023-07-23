"""
# Definition for a Node.

"""
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return []
        queue = collections.deque([root])
        while queue:
            l = len(queue)
            temp = []
            for _ in range(l):
                pop_node = queue.popleft()
                temp.append(pop_node.val)
                if not pop_node.children:
                    continue
                for child in pop_node.children:
                    queue.append(child)
            res.append(temp)
        return res
