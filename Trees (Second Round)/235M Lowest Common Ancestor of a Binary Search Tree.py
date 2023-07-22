# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#  Hint: search for the first value that is between p and q. That will be your lowest common ancestor

class Solution:
    def lowestCommonAncestor_re(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

    def lowestCommonAncestor_it(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
