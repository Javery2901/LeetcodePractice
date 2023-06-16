from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def valid(i, j, grid):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True

        def sub_island_compare(grid_list):
            for grid in grid_list:
                i, j = grid[0], grid[1]
                if grid1[i][j] != 1:
                    return False
            return True

        def dfs(i, j, visited):
            visited.add((i, j))
            grid2_list.append((i, j))
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if valid(x, y, grid2) and grid2[x][y] == 1 and (x, y) not in visited:
                    dfs(x, y, visited)

        grid2_visited = set()
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid1[2])):
                if grid2[i][j] == 1 and (i, j) not in grid2_visited:
                    grid2_list = []
                    dfs(i, j, grid2_visited)
                    if sub_island_compare(grid2_list):
                        count += 1
        return count


s = Solution()
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
test = s.countSubIslands(grid1, grid2)
print(test)