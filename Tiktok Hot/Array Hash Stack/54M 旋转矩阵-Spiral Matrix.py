from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # try to use dfs
        def valid(row, col):
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                return True
            return False

        def spiral(row, col, direction):
            if not valid(row, col) or matrix[row][col] == 101:
                return

            res.append(matrix[row][col])
            matrix[row][col] = 101
            if direction == 'right':
                spiral(row, col + 1, 'right')
                spiral(row + 1, col, 'down')
            if direction == 'down':
                spiral(row + 1, col, 'down')
                spiral(row, col - 1, 'left')
            if direction == 'left':
                spiral(row, col - 1, 'left')
                spiral(row - 1, col, 'up')
            if direction == 'up':
                spiral(row - 1, col, 'up')
                spiral(row, col + 1, 'right')

        res = []
        spiral(0, 0, 'right')
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(matrix))