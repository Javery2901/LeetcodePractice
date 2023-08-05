from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def valid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False

        def dfs(row, col):
            grid[row][col] = '0'
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if valid(r, c) and grid[r][c] == '1':
                    dfs(r, c)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(s.numIslands(grid))
