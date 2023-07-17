from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def position(index):
            row_num = index // col
            col_num = index % col
            return matrix[row_num][col_num] >= target

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col
        while left < right:
            mid = left + (right - left) // 2
            if position(mid):
                right = mid
            else:
                left = mid + 1
        # print(left)
        if left >= row * col:
            return False
        return matrix[left // col][left % col] == target


s = Solution()
matrix = [[1]]
target = 2
test = s.searchMatrix(matrix, target)
print(test)