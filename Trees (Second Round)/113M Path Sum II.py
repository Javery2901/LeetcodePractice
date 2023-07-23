# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # backtrack
        if not root:
            return []
        res = []

        def backtrack(root, ls, path_sum):
            if not root.left and not root.right:
                if path_sum + root.val == targetSum:
                    ls.append(root.val)
                    res.append(ls.copy())
                return
            if root.left:
                backtrack(root.left, ls + [root.val], path_sum + root.val)
            if root.right:
                backtrack(root.right, ls + [root.val], path_sum + root.val)

        backtrack(root, [], 0)
        return res

    def pathSum_it(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return res


