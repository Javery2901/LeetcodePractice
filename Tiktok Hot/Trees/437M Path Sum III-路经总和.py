# Definition for a binary tree node.
import collections
from typing import Optional
"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.count2 = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def path(root, target, is_root):
            if not root:
                return
            if root.val == target:
                self.count += 1
            path(root.left, target - root.val, False)
            path(root.right, target - root.val, False)
            # 判断是否是重新开始的节点。如果之前已经不是了，则不targetSum重新开始
            if is_root:
                path(root.left, targetSum, True)
                path(root.right, targetSum, True)

        path(root, targetSum, True)
        return self.count

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
         Maintain prefix sums while doing dfs from root to leaf.
         If currentSum-prefixSum=targetSum,
         then we've found a path that has a value of target.
         If we encountered prefixSum n times, then we've found n such paths.
        """
        hp = collections.defaultdict(int)

        def dfs(node, cur_sum):
            if not node:
                return
            cur_sum += node.val
            if cur_sum == targetSum:
                self.count2 += 1
            self.count2 += hp[cur_sum - targetSum]
            hp[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            hp[cur_sum] -= 1

        dfs(root, 0)
        print(hp)
        return self.count2

