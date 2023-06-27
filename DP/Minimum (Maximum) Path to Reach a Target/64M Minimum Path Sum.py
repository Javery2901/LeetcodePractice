from math import inf
from typing import List


class Solution:
    def minPathSum_top_down(self, grid: List[List[int]]) -> int:
        memo = {(0, 0): grid[0][0]}

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            return False

        def dfs(i, j, memo):
            if not valid(i, j):
                return inf
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = min(dfs(i - 1, j, memo), dfs(i, j - 1, memo)) + grid[i][j]
            return memo[(i, j)]

        i, j = len(grid), len(grid[-1])
        dfs(i - 1, j - 1, memo)
        # print(memo)
        return memo[(i - 1, j - 1)]

    def minPathSum_bottom_up(self, grid: List[List[int]]) -> int:
        table = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
        # print(table)
        for i in range(1, len(grid)):
            table[i][0] = table[i - 1][0] + table[i][0]
        for j in range(1,len(grid[0])):
            table[0][j] = table[0][j - 1] + table[0][j]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                table[i][j] = min(table[i - 1][j], table[i][j - 1]) + table[i][j]
        print(table)
        return table[-1][-1]


s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
test = s.minPathSum_bottom_up(grid)
print(test)
