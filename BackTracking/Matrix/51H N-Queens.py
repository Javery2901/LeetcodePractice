from typing import List
"""
time complexity: O(N!)
the solution space is reduce by 2 at each level in the exploration tree.
Space complexity: O(N^2)
recursive call stack to explore all possible solutions
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        diag_range = set()
        antidiag_range = set()
        col_range = set()

        def backtracking(row):
            # everytime row + 1
            if row == n:
                res.append([''.join(i) for i in board])
                return
            for col in range(n):
                if col in col_range or (row - col) in diag_range or (row + col) in antidiag_range:
                    continue

                col_range.add(col)
                diag_range.add(row - col)  # important
                antidiag_range.add(row + col)  # important
                board[row][col] = 'Q'
                backtracking(row + 1)

                col_range.remove(col)
                diag_range.remove(row - col)
                antidiag_range.remove(row + col)
                board[row][col] = '.'

        backtracking(0)
        return res



s = Solution()
n = 4
test = s.solveNQueens(n)
print(test)