# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # dfs
        ls = []

        def inorder_dfs(node, ls):
            if not node:
                return
            inorder_dfs(node.left, ls)
            ls.append(node.val)
            inorder_dfs(node.right, ls)

        inorder_dfs(root, ls)
        i = 0
        j = len(ls) - 1
        while i < j:
            if ls[i] + ls[j] == k:
                return True
            elif ls[i] + ls[j] > k:
                j -= 1
            else:
                i += 1
        return False

    def findTarget_bfs(self, root: Optional[TreeNode], k: int) -> bool:
        # time and space is O(n)
        queue = deque([root])

        seen = set()
        while queue:
            node = queue.popleft()
            if k - node.val in seen:
                return True
            if node.val not in seen:
                seen.add(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False

    def findTarget_dfs(self, root: Optional[TreeNode], k: int) -> bool:
        existed = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in existed:
                return True
            existed.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
