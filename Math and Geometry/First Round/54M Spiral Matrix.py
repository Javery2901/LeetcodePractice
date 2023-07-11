from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()

        def valid(i, j):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                return True

        def spiral(i, j, direction):
            if not valid(i, j) or (i, j) in visited:
                return
            visited.add((i, j))
            res.append(matrix[i][j])
            if direction == 'right':
                spiral(i, j + 1, 'right')
                spiral(i + 1, j, 'down')
            elif direction == 'down':
                spiral(i + 1, j, 'down')
                spiral(i, j - 1, 'left')
            elif direction == 'left':
                spiral(i, j - 1, 'left')
                spiral(i - 1, j, 'up')
            elif direction == 'up':
                spiral(i - 1, j, 'up')
                spiral(i, j + 1, 'right')

        spiral(0, 0, 'right')
        return res


s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test = s.spiralOrder(matrix)
print(test)