# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_value = min(p.val, q.val)
        q_value = max(p.val, q.val)
        node = root
        while node:
            if node.val < p_value:
                node = node.right
            elif p_value <= node.val <= q_value:
                return node
            else:
                node = node.left

