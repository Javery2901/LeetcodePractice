from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 从边缘开始dfs，如果有0，直接转换成1
        def valid(row, col):
            if 0 <= row < row_length and 0 <= col < col_length:
                return True
            return False

        def dfs(row, col):
            grid[row][col] = 1
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if valid(r, c) and grid[r][c] == 0:
                    dfs(r, c)

        row_length = len(grid)
        col_length = len(grid[0])
        for i in range(row_length):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][col_length - 1] == 0:
                dfs(i, col_length - 1)
        for j in range(col_length):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[row_length - 1][j] == 0:
                dfs(row_length - 1, j)
        # make sure all the lands adjacent to the edge is not closed island
        res = 0
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1

        return res

s = Solution()
grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print(s.closedIsland(grid))
