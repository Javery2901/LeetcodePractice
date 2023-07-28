from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def valid(row, col):
            if 0 <= row < row_length and 0 <= col < col_length:
                return True
            return False

        def dfs(row, col):
            grid[row][col] = 0
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if valid(r, c) and grid[r][c] == 1:
                    dfs(r, c)

        row_length = len(grid)
        col_length = len(grid[0])
        for i in range(row_length):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][col_length - 1] == 1:
                dfs(i, col_length - 1)
        for j in range(col_length):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[row_length - 1][j] == 1:
                dfs(row_length - 1, j)

        island_count = 0
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    island_count += 1
        return island_count


s = Solution()
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
test = s.numEnclaves(grid)
print(test)