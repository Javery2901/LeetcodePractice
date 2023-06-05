# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bfs
        res = 0
        queue = collections.deque([(root, root.val)])
        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                res += 1
            if node.left:
                queue.append((node.left, max(max_val, node.val)))
            if node.right:
                queue.append((node.right, max(node.val, max_val)))
            return res
