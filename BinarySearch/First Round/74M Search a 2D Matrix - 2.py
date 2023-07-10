"""
Runtime: ms70, beat 6%
Difficulty: Median
Solution: binary search
Time complexity: O(log(m+n))
Space complexity: O(1)
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: row += 1
            elif matrix[row][col] > target: col -= 1
        return False


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
res = sol.searchMatrix(matrix, target)
print(res)