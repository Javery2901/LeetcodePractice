from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = set()
        res = [0]
        obstacle = 0
        # count the number of -1:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    obstacle += 1

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            return False

        def backtrack(i, j, res):
            if not valid(i, j) or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                if len(visited) == len(grid) * len(grid[0]) - obstacle:
                    res[0] += 1
                return
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                backtrack(x, y, res)
                visited.remove((x, y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    backtrack(i, j, res)
                    return res[0]


s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
test = s.uniquePathsIII(grid)
print(test)