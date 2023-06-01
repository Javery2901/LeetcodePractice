from typing import List

'''
Difficulty: Median
Solution: Use three sets to record and check if the sudoku is valid
Time complexity: O(n2) n is the length of sudoku (Actually this is 2*n2)
Space complexity: O(n2) n is the length of sudoku (Actually this is 3*n2)
Analysis: This is not the optimal solution, but easy to understand
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            sudoku_set_row = set()
            sudoku_set_col = set()
            for j in range(len(board)):
                # print('i', i)
                # print('j', j)
                # print('board[i][j]', board[i][j])
                # print('board[j][i]', board[j][i])
                if board[i][j] in sudoku_set_row:
                    return False
                if board[j][i] in sudoku_set_col:
                    return False
                if board[i][j] != '.':
                    sudoku_set_row.add(board[i][j])
                if board[j][i] != '.':
                    sudoku_set_col.add(board[j][i])
                # print('sudoku_set_row', sudoku_set_row)

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                sudoku_set_cubic = set()
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        # print('i', i)
                        # print('j', j)
                        # print('board[i][j]', board[a][b])
                        if board[a][b] in sudoku_set_cubic:
                            return False
                        if board[a][b] != '.':
                            sudoku_set_cubic.add(board[a][b])
                        # print('sudoku_set_cubic', sudoku_set_cubic)
        return True


s = Solution()
board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
res = s.isValidSudoku(board)
print(res)