# Definition for a Node.
import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_dfs_it(self, node: 'Node') -> 'Node':
        if not node:
            return node
        new_node = Node(node.val)
        visited = {node: new_node}
        if not node.neighbors:
            return new_node

        def dfs(new_node, old_node):
            for old_neighbor in old_node.neighbors:
                if old_neighbor not in visited:
                    next_new_node = Node(old_neighbor.val)  # create new node

                    visited[old_neighbor] = next_new_node
                    new_node.neighbors.append(next_new_node)  # append

                    dfs(next_new_node, old_neighbor)
                else:
                    new_node.neighbors.append(visited[old_neighbor])
        dfs(new_node, node)
        return new_node

    def cloneGraph_dfs_stack(self, node: 'Node') -> 'Node':
        if not node:
            return node
        new_node = Node(node.val)
        visited = {node: new_node}
        if not node.neighbors:
            return new_node

        stack = [node]
        while stack:
            old_node = stack.pop()
            for old_neighbor in old_node.neighbors:
                if old_neighbor not in visited:
                    next_new_node = Node(old_neighbor.val)
                    visited[old_neighbor] = next_new_node
                    visited[old_node].neighbors.append(next_new_node)
                    stack.append(old_neighbor)
                else:
                    visited[old_node].neighbors.append(visited[old_neighbor])

        return new_node

    def cloneGraph_bfs_queue(self, node: 'Node') -> 'Node':
        if not node:
            return node
        new_node = Node(node.val)
        visited = {node: new_node}
        if not node.neighbors:
            return new_node

        queue = collections.deque([node])
        while queue:
            old_node = queue.popleft()
            for old_neighbor in old_node.neighbors:
                if old_neighbor not in visited:
                    next_new_node = Node(old_neighbor.val)
                    visited[old_neighbor] = next_new_node
                    visited[old_node].neighbors.append(next_new_node)
                    queue.append(old_neighbor)
                else:
                    visited[old_node].neighbors.append(visited[old_neighbor])

        return new_node









