import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # let's know the number of 0
        # only can use bfs

        def valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True

        output = -1
        count_zero = 0
        queue = collections.deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    count_zero += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        # now we have all initial 2 in queue, loop
        if not queue:
            if count_zero < len(grid) * len(grid[0]):
                return -1
            else:
                return 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                visited.add((i, j))
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if valid(x, y) and grid[x][y] == 1 and (x, y) not in visited:
                        grid[x][y] = 2
                        queue.append((x, y))
            output += 1

        if len(visited) + count_zero < len(grid) * len(grid[0]):
            return -1
        else:
            return output


s = Solution()
grid = [[0,2]]
test = s.orangesRotting(grid)
print(test)
