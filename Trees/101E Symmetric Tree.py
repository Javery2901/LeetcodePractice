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
                    return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
            elif r1 or r2:  # if one of them exists
                return False
            else:  # if they are all empty
                return True
        return dfs(r1, r2)

    def isSymmetric_it(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        r1, r2 = root, root
        stack = [(r1, r2)]
        while stack:
            node1, node2 = stack.pop()
            if node1.left and node2.right:
                if node1.left.val == node2.right.val:
                    stack.append((node1.left, node2.right))
                else:
                    return False
            if node1.right and node2.left:
                if node1.right.val == node2.left.val:
                    stack.append((node1.right, node2.left))
                else:
                    return False
            if (node1.left and not node2.right) or (not node1.left and node2.right):
                return False
            if (node1.right and not node2.left) or (not node1.right and node2.left):
                return False
        return True


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.right = TreeNode(76)
node.right.left = TreeNode(76)
node.left.right.right = TreeNode(13)
node.right.left.right = TreeNode(13)
s = Solution()
print(s.isSymmetric(node))