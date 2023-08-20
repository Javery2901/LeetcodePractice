from typing import List
"""
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def position(index):
            row_num = index // col
            col_num = index % col
            return matrix[row_num][col_num] >= target

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left < right:
            mid = left + (right - left) // 2
            if position(mid):
                right = mid
            else:
                left = mid + 1
        return matrix[left // col][left % col] == target


s = Solution()
matrix = [[1]]
target = 2
test = s.searchMatrix(matrix, target)
print(test)