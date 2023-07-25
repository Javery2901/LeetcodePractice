from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def valid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False

        def backtracking(row, col, path):
            if grid[row][col] == 2 and len(path) == len(grid) * len(grid[0]) - obstacle:
                res[0] += 1
                return
            for r, c in ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)):
                if not valid(r, c) or (r, c) in visited or grid[r][c] == -1:
                    continue

                visited.add((r, c))
                path.append((r, c))
                backtracking(r, c, path)
                visited.remove((r, c))
                path.pop()

        res = [0]
        obstacle = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == -1:
                    obstacle += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    visited = {(i, j)}
                    path = [(i, j)]
                    backtracking(i, j, path)
        return res[0]


s = Solution()
grid = [[0,1],[2,0]]
test = s.uniquePathsIII(grid)
print(test)
