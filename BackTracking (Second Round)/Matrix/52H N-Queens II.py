class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0]
        board = [[0] * n for _ in range(n)]
        col_check = set()
        diag_check = set()
        antidiag_check = set()

        def backtracking(row):
            if row == n:
                res[0] += 1
                return
            for col in range(n):
                if col in col_check or (row - col) in diag_check or (row + col) in antidiag_check:
                    continue
                board[row][col] = 1
                col_check.add(col)
                diag_check.add(row - col)
                antidiag_check.add(row + col)

                backtracking(row + 1)

                board[row][col] = 0
                col_check.remove(col)
                diag_check.remove(row - col)
                antidiag_check.remove(row + col)

        backtracking(0)
        return res[0]


s = Solution()
n = 4
test = s.totalNQueens(n)
print(test)
