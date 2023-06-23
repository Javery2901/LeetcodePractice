"""
This comes from leetcode 48M, rotate array 90, 180, 270, 360 degree
"""

class Solution:
    def rotate_inplace(self, matrix: List[List[int]]) -> None:
        """
        从四个角开始换，每边需要换n-1个点，整个边换完后向内缩，向内缩进的次数为 len(matrix) // 2
        从最外圈开始，向内缩进运行。每缩进一轮，运行次数为n - r * 2 - 1
        根据90, 180, 270, 360等不同转法的需要更改转动对象
        """
        n = len(matrix)
        layer = n // 2

        def layer_swap(n, r):
            for i in range(n - r * 2 - 1):
                # eg: n == 8时, round 0: 最外层，range(7) 每边有7个点需要旋转
                # eg: n == 8时, round 1: 第二层，range(5) 每边有5个点需要旋转
                # eg: n == 8时, round 3: 第三层，range(3) 每边有3个点需要旋转
                # eg: n == 8时, round 4: 第四层，range(1) 每边有1个点需要旋转 exit
                matrix[r][i + r], matrix[i + r][n - 1 - r], matrix[n - 1 - r][n - 1 - r - i], matrix[n - 1 - r - i][r]= \
                    matrix[n - 1 - r - i][r], matrix[r][i + r], matrix[i + r][n - 1 - r], matrix[n - 1 - r][n - 1 - r - i]
                # 第一轮即i==0时，分别是 最左上角，最右上角，最右下角，最左下角 = 最左下角， 最左上角，最右上角，最右下角
                # 从而完成四个点的90度顺时针更换
        for round in range(layer):
            layer_swap(n, round)


s = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate_inplace(matrix)
print(matrix)