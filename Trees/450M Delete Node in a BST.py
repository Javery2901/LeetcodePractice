# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr

        if not root:
            return
        # find the root first
        if root.val > key:
            self.deleteNode(root.left, key)
        elif root.val < key:
            self.deleteNode(root.right, key)
        else:
            # now we find the node
            # no child
            if not root.left and not root.right:
                root = None
            # 1 child
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            # 2 children, we can either replace root's val with min of right, or max of left
            else:
                temp = find_min(root.right)  # find min of right
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
