from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs: 当周围是1时返回0， 是0或不存在时范围1，四个边相加

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True

        def dfs(i, j):
            if not valid(i, j) or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1)

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)


s = Solution()
grid = [[1,1],[1,1]]
test = s.islandPerimeter(grid)
print(test)
