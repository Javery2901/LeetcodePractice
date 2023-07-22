# Definition for a binary tree node.
from typing import Optional


# how the hell is this labelled easy?
# same as leetcode 124

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 思路：创建self.diameter,遍历每个节点，找到每个结点的高度，最下面为1，往上逐层加1
        # 保存每次的节点相加的最大值，即为所求的路线商都
        def max_height(node):
            if not node:
                return 0
            left_height = max_height(node.left)
            right_height = max_height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        max_height(root)
        return self.diameter



