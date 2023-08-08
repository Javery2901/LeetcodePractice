from math import sqrt
from typing import List


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
