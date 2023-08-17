# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        queue = [root]
        while queue:
            next_queue = []
            for node in queue:
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                res.append('.' if not node else str(node.val))
            queue = next_queue
        return ' '.join(res)  # '1 2 3 . . 4 5 . . . . '  # 有可能出现负数

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split()
        root = TreeNode(int(data[0]))
        index = 1
        queue = collections.deque([root])
        while queue:
            pop_node = queue.popleft()
            if data[index] != '.':
                pop_node.left = TreeNode(int(data[index]))
                queue.append(pop_node.left)
            index += 1
            if data[index] != '.':
                pop_node.right = TreeNode(int(data[index]))
                queue.append(pop_node.right)
            index += 1
        return root


