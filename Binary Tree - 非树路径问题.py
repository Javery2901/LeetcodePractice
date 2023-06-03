"""
复杂度 O(n)
自己总结：
以 leetcode 543. Diameter of Binary Tree and 124. Binary Tree Maximum Path Sum为例
这类问题需要在树的递归过程中记录下某个链条的特点，如求最长的路径，或路径上的节点最大和等问题
这类问题使用循环遍历实现相对来说比较困难。循环遍历二叉树需要使用栈或队列等数据结构来保存待访问的节点。
但链条计算涉及到对每个节点子树的递归计算，这使得使用循环遍历实现相对复杂。
思路：使用了深度优先搜索（DFS）的思想来遍历二叉树。通过递归地计算每个节点的某个特点，同时更新其特点，最终得到想要的结果
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.value_updated_every_recursion = None

    def linkageOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 思路：创建self.value_updated_every_recursion,保存每次递归时的某要计算
        # 在这种方式下，求得的某个值可以由树的链条构成，而不局限于字母关系
        def dfs_recursion(node):
            if not node:
                return 0  # Return some value based on requirement
            left = dfs_recursion(node.left)
            right = dfs_recursion(node.right)
            self.value_updated_every_recursion = max(self.value_updated_every_recursion, left, right)
            # value_updated_every_recursion to be updated based on requirement
            return max(left, right)  # return some value based on requirement

        dfs_recursion(root)
        return self.value_updated_every_recursion
