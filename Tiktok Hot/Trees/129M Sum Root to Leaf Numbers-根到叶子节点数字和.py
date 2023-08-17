# Definition for a binary tree node.
from typing import Optional
"""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # try dfs

        def branch(node, number):
            if node and not node.left and not node.right:
                self.res += number * 10 + node.val
                print(self.res, node.val)
                return
            number += number * 10 + node.val
            if node.left:
                branch(node.left, number)
            if node.right:
                branch(node.right, number)

        branch(root, 0)
        return self.res


