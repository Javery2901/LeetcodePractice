from typing import List
"""
time complexity: O(N!)
the solution space is reduce by 2 at each level in the exploration tree.
Space complexity: O(N^2)
recursive call stack to explore all possible solutions
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ls = [['.'] * n for _ in range(n)]
        res = []
        horizontal_range = set()
        diag_range = set()
        antidiag_range = set()

        def dfs_backtracking(col, index):
            # everytime col + 1
            if index == n:
                res.append([''.join(i) for i in ls])
                return

            for r in range(n):
                if r in horizontal_range or (r - col) in diag_range or (r + col) in antidiag_range:
                    continue
                ls[r][col] = 'Q'
                horizontal_range.add(r)
                diag_range.add(r - col)
                antidiag_range.add(r + col)

                dfs_backtracking(col + 1, index + 1)

                horizontal_range.remove(r)
                diag_range.remove(r - col)
                antidiag_range.remove(r + col)
                ls[r][col] = '.'

        dfs_backtracking(0, 0)
        return res


s = Solution()
n = 4
test = s.solveNQueens(n)
print(test)
