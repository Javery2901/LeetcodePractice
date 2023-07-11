from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_added = set()  # all the new set 0 will not be considered

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 and (i, j) not in new_added:
                    new_added.add((i, j))

        row_zero = set()
        col_zero = set()
        for i, j in new_added:
            if i not in row_zero:
                row_zero.add(i)
                for _ in range(len(matrix[i])):
                    matrix[i][_] = 0
            if j not in col_zero:
                col_zero.add(j)
                for _ in range(len(matrix)):
                    matrix[_][j] = 0


s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix)