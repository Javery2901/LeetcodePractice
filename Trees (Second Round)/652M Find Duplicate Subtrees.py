# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # idea: 用字典记录 {subtree: 1} 当有节点值相同时，加入res
        # subtree用tuple形式记录
        res = []
        dic = collections.defaultdict(int)

        def dfs(root):
            if not root:
                return
            sub = tuple([dfs(root.left), root.val, dfs(root.right)])
            if sub in dic and dic[sub] == 1:
                res.append(root)
            dic[sub] += 1
            return sub

        dfs(root)
        return res