# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p_path = []
        self.q_path = []
        self.count = 0

    def lowestCommonAncestor_backtracking(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # use dfs backtracking to find the path of each node
        path = []

        def backtracking(root, path):
            if self.count == 2:
                return
            path.append(root)
            if root == p:
                self.p_path = path[:]
                self.count += 1
            if root == q:
                self.q_path = path[:]
                self.count += 1

            if root.left:
                backtracking(root.left, path)
            if root.right:
                backtracking(root.right, path)
            path.pop()

        backtracking(root, path)
        q_set = set(self.q_path)
        for i in range(len(self.p_path) - 1, -1, -1):
            if self.p_path[i] in q_set:
                return self.p_path[i]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r  # if they are both none, return none, if one of them exist, return the one





