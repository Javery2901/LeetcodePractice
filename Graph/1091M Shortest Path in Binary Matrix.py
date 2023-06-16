import collections
from typing import List
"""
可以优化，使用heapq，从最后一个往前
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # bfs, start from (0, 0)

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid):
                return True

        queue = collections.deque([(0, 0)])
        visited = {(0, 0)}
        lvl = 0
        while queue:
            lvl += 1
            for _ in range(len(queue)):
                pop_node = queue.popleft()
                i, j = pop_node[0], pop_node[1]
                for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                             (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)):
                    if x == len(grid) - 1 and y == len(grid) - 1:
                        return lvl + 1
                    if valid(x, y) and grid[x][y] == 0 and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
        if (len(grid) - 1, len(grid) - 1) not in visited:
            return -1
        return lvl



s = Solution()
grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
test = s.shortestPathBinaryMatrix(grid)
print(test)
