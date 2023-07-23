"""
# Definition for a Node.
"""
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # try use bfs
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            if len(queue) == 1:
                pop_node = queue.popleft()
                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            else:
                l = len(queue)
                prev = queue.popleft()
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
                for _ in range(l - 1):
                    curr = queue.popleft()
                    prev.next = curr
                    if prev.left:
                        queue.append(prev.left)
                    if prev.right:
                        queue.append(prev.right)
                    prev, curr = curr, None
        return root
