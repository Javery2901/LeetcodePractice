# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 使用下标而不是切片，可以更加节约时间和空间
        if not nums:
            return
        node = TreeNode(max(nums))
        index = nums.index(node.val)
        node.left = self.constructMaximumBinaryTree(nums[: index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return node