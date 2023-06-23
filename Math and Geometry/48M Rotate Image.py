from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        从四个角开始换，loop一次，然后向内缩，直到内部长度<=1
        """
        n = len(matrix)
        layer = n // 2

        def layer_swap(n, r):
            # n = 长度，eg: matrix = 4, 第一轮，n = 4， 第二轮，n = 2， 第三轮，n = 0， 结束
            # round: 轮数，eg: matrix = 4, round = 0，start = [0][0], 下一轮， start = [1][1]
            # 对这一层来说，需要换n-1次（一排的起点到终点前的一个数），每次是四个点交换
            for i in range(n - r * 2 - 1):
                # n == len(matrix) == 8, round 0: range(7)
                # n == len(matrix) == 8, round 1: range(5)
                # n == len(matrix) == 8, round 3: range(3)
                # n == len(matrix) == 8, round 4: range(1)  exit
                matrix[r][i + r], matrix[i + r][n - 1 - r], matrix[n - 1 - r][n - 1 - r - i], matrix[n - 1 - r - i][r]= \
                    matrix[n - 1 - r - i][r], matrix[r][i + r], matrix[i + r][n - 1 - r], matrix[n - 1 - r][n - 1 - r - i]

        for round in range(layer):
            layer_swap(n, round)


s = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(matrix)
print(matrix)
