import math
from typing import List

"""
because of negative, we cant start from top left, instead we need to start from bottom right
(IT5005) inspired
"""


class Solution:
    def calculateMinimumHP_top_down(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # m: row, n: col
        memo = {(m - 1, n - 1): 1 if dungeon[m - 1][n - 1] >= 0 else 1 - dungeon[m - 1][n - 1]}

        # memo: record the min health that position needed

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        def sub_min_hp(i, j, memo):
            if not valid(i, j):
                return math.inf
            if (i, j) in memo:
                return memo[(i, j)]
            if dungeon[i][j] >= min(sub_min_hp(i, j + 1, memo), sub_min_hp(i + 1, j, memo)):
                memo[(i, j)] = 1
            else:
                memo[(i, j)] = min(sub_min_hp(i, j + 1, memo), sub_min_hp(i + 1, j, memo)) - dungeon[i][j]
            return memo[(i, j)]

        return sub_min_hp(0, 0, memo)

    def calculateMinimumHP_bottom_down(self, dungeon: List[List[int]]) -> int:
        table = [[dungeon[i][j] for j in range(len(dungeon[i]))] for i in range(len(dungeon))]
        m, n = len(dungeon), len(dungeon[0])
        table[m - 1][n - 1] = 1 if table[m - 1][n - 1] >= 0 else -table[m - 1][n - 1] + 1

        for i in range(m - 2, -1, -1):
            table[i][-1] = table[i + 1][-1] - table[i][-1] if table[i + 1][-1] > table[i][-1] else 1

        for j in range(n - 2, -1, -1):
            table[-1][j] = table[-1][j + 1] - table[-1][j] if table[-1][j + 1] > table[-1][j] else 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if min(table[i][j + 1], table[i + 1][j]) > table[i][j]:
                    table[i][j] = min(table[i][j + 1], table[i + 1][j]) - table[i][j]
                else:
                    table[i][j] = 1
        return table[0][0]


s = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
test = s.calculateMinimumHP_bottom_down(dungeon)
print(test)
