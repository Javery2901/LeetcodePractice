# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # bfs
        # find the number of node first
        # then traverse again, check when we first counter a node who does not have one child,
        # check if this is the last one
        count = 0
        queue = collections.deque([root])
        while queue:
            pop_node = queue.popleft()
            count += 1
            if pop_node.left:
                queue.append(pop_node.left)
            if pop_node.right:
                queue.append(pop_node.right)
        # now we now the number of tree
        queue.append(root)
        i = 1
        while queue:
            pop_node = queue.popleft()
            if pop_node.left:
                queue.append(pop_node.left)
                i += 1
            else:
                return True if i == count else False
            if pop_node.right:
                queue.append(pop_node.right)
                i += 1
            else:
                return True if i == count else False

    def isCompleteTree_2(self, root: TreeNode) -> bool:
        end = False
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                end = True
            else:
                if end:
                    return False
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return True
