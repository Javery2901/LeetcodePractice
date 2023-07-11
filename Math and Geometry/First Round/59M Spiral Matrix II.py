from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        def valid(i, j):
            if 0 <= i < n and 0 <= j < n:
                return True

        def spiral(i, j, num, direction):
            if not valid(i, j) or res[i][j] != 0:
                return
            res[i][j] = num
            if direction == 'right':
                spiral(i, j + 1, num + 1, 'right')
                spiral(i + 1, j, num + 1, 'down')
            elif direction == 'down':
                spiral(i + 1, j, num + 1, 'down')
                spiral(i, j - 1, num + 1, 'left')
            elif direction == 'left':
                spiral(i, j - 1, num + 1, 'left')
                spiral(i - 1, j, num + 1, 'up')
            elif direction == 'up':
                spiral(i - 1, j, num + 1, 'up')
                spiral(i, j + 1, num + 1, 'right')

        spiral(0, 0, 1, 'right')
        return res


s = Solution()
n = 1
test = s.generateMatrix(n)
print(test)
