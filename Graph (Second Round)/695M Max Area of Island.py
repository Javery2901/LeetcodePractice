import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_num = 0

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True

        def dfs_re(i, j):
            nonlocal num
            if not valid(i, j) or (i, j) in visited:
                return
            if grid[i][j] == 1:
                visited.add((i, j))
                num += 1
                dfs_re(i + 1, j)
                dfs_re(i - 1, j)
                dfs_re(i, j + 1)
                dfs_re(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    num = 0
                    dfs_re(i, j)
                    max_num = max(num, max_num)
        return max_num

    def maxAreaOfIsland_bfs(self, grid: List[List[int]]) -> int:
        max_res = 0
        # go bfs
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    queue = collections.deque([(i, j)])
                    while queue:
                        row, col = queue.popleft()
                        for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 0:
                                continue
                            area += 1
                            grid[r][c] = 0
                            queue.append((r, c))
                    max_res = max(max_res, area)

        return max_res


s = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
test = s.maxAreaOfIsland(grid)
print(test)