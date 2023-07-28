import collections

from cmath import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs
        # 0 - 1

        def valid(row, col):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return True
            return False

        visited = set()
        res = [[inf] * len(mat[0]) for _ in range(len(mat))]
        queue = collections.deque([])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            row, col, layer = queue.popleft()
            visited.add((row, col))
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if valid(r, c) and (r, c) not in visited and mat[r][c] == 1:
                    res[r][c] = min(res[r][c], layer + 1)
                    visited.add((r, c))
                    queue.append((r, c, layer + 1))
        return res

    def updateMatrix_dp(self, mat: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/
        # dp. first 从左上到右下，第二次从右下到左上
        m, n = len(mat), len(mat[0])

        # to right bottom
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r >= 1 else math.inf
                    left = mat[r][c - 1] if c >= 1 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(bottom + 1, right + 1, mat[r][c])

        return mat


s = Solution()
mat = [[0],[0],[0],[0],[0]]
test = s.updateMatrix(mat)
print(test)