from typing import List
from collections import deque
# use dict instead of set

class Solution:
    def isBipartite_bfs(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            queue = deque()
            if i not in color:
                color[i] = 1
                queue.append(i)
            while queue:
                pop_node = queue.popleft()
                for neighbor_node in graph[pop_node]:
                    if neighbor_node not in color:
                        color[neighbor_node] = color[pop_node] * -1
                        queue.append(neighbor_node)
                    elif color[neighbor_node] == color[pop_node]:
                        return False
        return True

    def isBipartite_dfs(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            stack = []
            if i not in color:
                color[i] = 1
                stack.append(i)
            while stack:
                pop_node = stack.pop()
                for neighbor_node in graph[pop_node]:
                    if neighbor_node not in color:
                        color[neighbor_node] = color[pop_node] * -1
                        stack.append(neighbor_node)
                    elif color[neighbor_node] == color[pop_node]:
                        return False
        return True

    def isBipartite_dfs_re(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node, col):
            color[node] = col
            for next_node in graph[node]:
                if next_node in color:
                    if color[node] == color[next_node]:
                        return False
                else:
                    if not dfs(next_node, col * -1):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                if not dfs(i, 1):
                    return False
        return True


s = Solution()
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
test1 = s.isBipartite_bfs(graph)
print(test1)
test2 = s.isBipartite_dfs(graph)
print(test2)
test3 = s.isBipartite_dfs_re(graph)
print(test3)
