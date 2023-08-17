import math
from typing import List
"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
"""

class Solution:
    def minimumTotal_top_down(self, triangle: List[List[int]]) -> int:
        memo = {(0, 0): triangle[0][0]}

        def valid(i, j):
            if 0 <= i < len(triangle) and 0 <= j < len(triangle[i]):
                return True
            return False

        def sub_min_total(i, j, memo):
            if not valid(i, j):
                return math.inf
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = min(sub_min_total(i - 1, j - 1, memo), sub_min_total(i - 1, j, memo)) + triangle[i][j]
            return memo[(i, j)]

        n = len(triangle)
        m = len(triangle[n - 1])
        return min(sub_min_total(n - 1, j, memo) for j in range(m))

    def minimumTotal_bottom_up(self, triangle: List[List[int]]) -> int:
        table = [[triangle[i][j] for j in range(len(triangle[i]))] for i in range(len(triangle))]
        # print(table)  # deep copy
        for i in range(1, len(triangle)):
            table[i][0] += table[i - 1][0]
            table[i][-1] += table[i - 1][-1]
        for i in range(1, len(triangle)):
            for j in range(1, len(triangle[i]) - 1):
                table[i][j] += min(table[i - 1][j - 1], table[i - 1][j])
        # print(table)
        return min(table[len(triangle) - 1][j] for j in range(len(triangle[-1])))


s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
test = s.minimumTotal_bottom_up(triangle)
print(test)