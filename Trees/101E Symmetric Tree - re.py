# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        r1, r2 = root, root

        def dfs(r1, r2):
            if r1 and r2:  # if they both exist
                if r1.val != r2.val:
                    return False
                else:
                    return True and dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
            elif r1 or r2:  # if one of them exists
                return False
            else:  # if they are all empty
                return True
        return dfs(r1, r2)


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.right = TreeNode(76)
node.right.left = TreeNode(76)
node.left.right.right = TreeNode(13)
node.right.left.right = TreeNode(13)
s = Solution()
print(s.isSymmetric(node))