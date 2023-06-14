from typing import List
from collections import deque


class Solution:
    def numIslands_bfs_it(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            return False

        def bfs(i, j, visited):
            to_visit = deque([(i, j)])
            visited.add((i, j))
            while to_visit:
                r, c = to_visit.popleft()
                if valid(r - 1, c) and grid[r - 1][c] == '1' and (r - 1, c) not in visited:
                    to_visit.append((r - 1, c))
                    visited.add((r - 1, c))
                if valid(r + 1, c) and grid[r + 1][c] == '1' and (r + 1, c) not in visited:
                    to_visit.append((r + 1, c))
                    visited.add((r + 1, c))
                if valid(r, c - 1) and grid[r][c - 1] == '1' and (r, c - 1) not in visited:
                    to_visit.append((r, c - 1))
                    visited.add((r, c - 1))
                if valid(r, c + 1) and grid[r][c + 1] == '1' and (r, c + 1) not in visited:
                    to_visit.append((r, c + 1))
                    visited.add((r, c + 1))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    bfs(i, j, visited)
        return count

    def numIslands_dfs_re(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            grid[i][j] = '0'
            if i > 0 and grid[i - 1][j] == '1':
                dfs(i - 1, j)
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                dfs(i, j + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count


s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
test = s.numIslands_bfs_it(grid)
print(test)
test2 = s.numIslands_dfs_re(grid)
print(test2)
