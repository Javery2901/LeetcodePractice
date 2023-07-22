# Definition for a binary tree node.
import collections

from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.good_number = 0

    def goodNodes_re(self, root: TreeNode) -> int:
        max_val = -inf

        def dfs(root, max_val):
            if not root:
                return
            if root.val >= max_val:
                self.good_number += 1
                max_val = root.val
            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, max_val)
        return self.good_number

    def goodNodes(self, root: TreeNode) -> int:
        # dfs 同枝上记录一个最大值
        max_value = root.val

        def dfs(root, max_value):
            if not root:
                return 0
            if root.val >= max_value:
                return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
            elif root.val < max_value:
                return dfs(root.left, max_value) + dfs(root.right, max_value)

        return dfs(root, max_value)

    def goodNodes_it(self, root: TreeNode) -> int:
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
