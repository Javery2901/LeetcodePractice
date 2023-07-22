# Definition for a binary tree node.
from cmath import inf

import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if left < node.val < right:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            else:
                return False
        return valid(root, -sys.maxsize, sys.maxsize)

    def isValidBST_re(self, root: Optional[TreeNode]) -> bool:
        # 前一个和有一个比较，用一个常量变量记录前一个数
        def dfs(root):
            if not root:
                return True
            if not (dfs(root.left) and self.prev < root.val):
                return False
            self.prev = root.val
            return dfs(root.right)
        return dfs(root)

    def isValidBST_it1(self, root: Optional[TreeNode]) -> bool:
        # inorder
        if not root:
            return True
        left_min = float('-inf')
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if left_min >= node.val:
                        return False
                    else:
                        left_min = node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return True

    def isValidBST_it2(self, root: Optional[TreeNode]) -> bool:
        # inorder
        left_min = float('-inf')
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if left_min >= node.val:
                return False
            else:
                left_min = node.val
            cur = node.right
        return True





