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

        def lca(root, p_value, q_value):
            if root.val < p_value:
                return lca(root.right, p_value, q_value)
            elif p_value <= root.val <= q_value:
                return root
            else:
                return lca(root.left, p_value, q_value)

        return lca(root, p_value, q_value)
