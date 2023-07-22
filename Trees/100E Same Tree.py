# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree_re(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # else if one of p and q are empty, return False
        if not (p and q):
            return False
        if p.val == q.val and self.isSameTree_re(p.left, q.left) and self.isSameTree_re(p.right, q.right):
            return True
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q are both empty, return True
        if not p and not q:
            return True
        # else if one of p and q are empty, return False
        if not (p and q):
            return False
        # p, q must exist
        queue = collections.deque([(p, q)])
        while queue:
            p_node, q_node = queue.popleft()
            if p_node.val != q_node.val:
                return False
            if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
                # p and q are both empty, or one of them are empty
                return False
            if p_node.left and q_node.left:
                queue.append((p_node.left, q_node.left))
            if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
                return False
            if p_node.right and q_node.right:
                queue.append((p_node.right, q_node.right))
        return True








