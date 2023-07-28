import collections
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # traverse first, check if grid has 1 and 0
        # bfs, append all 1, layer by layer
        land_set = []
        water_set = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    land_set.append((i, j))
                else:
                    water_set.append((i, j))
        if not land_set or not water_set:
            return -1

        layer = -1
        queue = collections.deque(land_set)
        while queue:
            layer += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for r, c in ((row + 1, col), (row - 1, col), (row, col + 1),(row, col - 1)):
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                        grid[r][c] = 1
                        queue.append((r, c))
        return layer


s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,0]]
test = s.maxDistance(grid)
print(test)