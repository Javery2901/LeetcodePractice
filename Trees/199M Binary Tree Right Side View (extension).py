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

    # extension
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
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
                if i == 0:
                    res.append(pop_node.val)
        return res

    def topSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            pop_node = stack.pop()
            res.append(pop_node.val)
            if pop_node.left:
                stack.append(pop_node.left)
        res.reverse()
        stack = [root]
        while stack:
            pop_node = stack.pop()
            if pop_node != root:
                res.append(pop_node.val)
            if pop_node.right:
                stack.append(pop_node.right)
        return res

    def bottomSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            pop_node = stack.pop()
            if not pop_node.left or not pop_node.right:
                res.append(pop_node.val)
            if pop_node.right:
                stack.append(pop_node.right)
            if pop_node.left:
                stack.append(pop_node.left)
        return res

