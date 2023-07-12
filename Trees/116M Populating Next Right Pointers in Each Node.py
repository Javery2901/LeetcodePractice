"""
# Definition for a Node.
"""
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_bfs(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                pop_node = queue.popleft()
                level.append(pop_node)

                if pop_node.left:
                    queue.append(pop_node.left)
                if pop_node.right:
                    queue.append(pop_node.right)
            for i in range(0, len(level) - 1):
                level[i].next = level[i + 1]
        return root

    def connect_dfs(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            if not node:
                return
            node.left.next = node.right
            if not node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root

n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)
n.left.right = Node(5)
s = Solution()
s.connect_bfs(n)
print(n.next)
print(n.left.next.val)
print(n.right.next)




