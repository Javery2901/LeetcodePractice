from math import sqrt
from typing import List
"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalSquare_bottom_up(self, matrix: List[List[str]]) -> int:
        table = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_num = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    table[i][j] = 0
                else:
                    min_neighbor = min(table[i - 1][j], table[i - 1][j - 1], table[i][j - 1])
                    table[i][j] = min_neighbor + 1
                    max_num = max(max_num, table[i][j])
        return max_num ** 2


s = Solution()
matrix = [["0","1"],["1","0"]]
test = s.maximalSquare_bottom_up(matrix)
print(test)
