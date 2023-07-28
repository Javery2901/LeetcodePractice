import collections
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find the first island, and the surrounding water
        # bfs water one layer by one layer, until it touches the second island
        # 边缘水加入queue能提高效率
        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid):
                return True

        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if valid(x, y):
                    if grid[x][y] == 0 and (x, y) not in water:
                        water.add((x, y))
                    elif grid[x][y] == 1 and (x, y) not in visited:
                        dfs(x, y)

        visited = set()
        water = set()
        # use dfs
        first_island = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    first_island = True
                    dfs(i, j)
                if first_island:
                    break
            if first_island:
                break

        lvl = 0
        queue = collections.deque(list(water))
        while queue:
            lvl += 1
            for _ in range(len(queue)):
                pop_water = queue.popleft()
                i, j = pop_water[0], pop_water[1]
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if valid(x, y):
                        if grid[x][y] == 0 and (x, y) not in water:
                            water.add((x, y))
                            queue.append((x, y))
                        if grid[x][y] == 1 and (x, y) not in visited:
                            return lvl


s = Solution()
grid = [[0,1,0],[0,0,0],[0,0,1]]
test = s.shortestBridge(grid)
print(test)