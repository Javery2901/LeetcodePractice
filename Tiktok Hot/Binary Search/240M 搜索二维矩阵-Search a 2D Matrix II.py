from typing import List
"""
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(row, left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return matrix[row][left] == target
            # return False

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            if matrix[i][0] <= target <= matrix[i][-1]:
                if binary_search(i, 0, len(matrix[0]) - 1, target):
                    return True


s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 15
test = s.searchMatrix(matrix, target)
print(test)