from typing import List


class Solution:
    def uniquePathsWithObstacles_bottom_up(self, obstacleGrid: List[List[int]]) -> int:
        # all the '1' can be considered that the number of path going through is 0
        # 可优化为一维数组，space O(n)
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0] * (1 + n) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    table[i][j] = 0
                elif i == 1 and j == 1:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m][n]

    def uniquePathsWithObstacles_top_down(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True

        def sub_unique_paths(i, j, memo):
            if not valid(i, j) or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = sub_unique_paths(i - 1, j, memo) + sub_unique_paths(i, j - 1, memo)
            return memo[(i, j)]

        return sub_unique_paths(m - 1, n - 1, memo)


s = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
test = s.uniquePathsWithObstacles_top_down(obstacleGrid)
print(test)