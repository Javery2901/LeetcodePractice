# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        level_list = []
        level_count = 0  # count the current level
        queue = collections.deque([(root, 0)])
        while queue:
            pop_node, level = queue.popleft()
            if level == level_count:
                level_list.append(pop_node.val)
            else:
                res.append(level_list)
                level_list = [pop_node.val]
                level_count += 1
            if pop_node.left:
                queue.append((pop_node.left, level + 1))
            if pop_node.right:
                queue.append((pop_node.right, level + 1))
        res.append(level_list)
        res.reverse()
        return res


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
s = Solution()
s.levelOrderBottom(node)
print(s.levelOrderBottom(node))