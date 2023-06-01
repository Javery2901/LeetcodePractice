"""
Runtime: ms57, beat 33%
Difficulty: Median
Solution: binary search
Time complexity: O(log(mn))
Space complexity: O(1)
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        while start <= end:
            # print(start, end)
            mid_row = (start + end) // 2 // len(matrix[0])
            # print('mid_row =', mid_row)
            mid_col = ((start + end) // 2) - (mid_row * len(matrix[0]))
            # print('mid_col =', mid_col)
            # print('mid =', matrix[mid_row][mid_col])
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                start = (start + end) // 2 + 1
            else:
                end = (start + end) // 2 -1
        return False


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
res = sol.searchMatrix(matrix, target)
print(res)