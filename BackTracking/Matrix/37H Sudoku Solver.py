import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # create set
        row_check = collections.defaultdict(set)
        col_check = collections.defaultdict(set)
        cube_check = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    row_check[i].add(board[i][j])
                    col_check[j].add(board[i][j])
                    cube_check[(i // 3, j // 3)].add(board[i][j])

        def backtracking(board):
            for row in range(len(board)):  # for loop: row
                for col in range(len(board[0])):
                    if board[row][col] != '.':
                        continue
                    for k in range(1, 10):
                        if str(k) in row_check[row] or str(k) in col_check[col] or str(k) in cube_check[(row // 3, col // 3)]:
                            continue
                        board[row][col] = str(k)
                        row_check[row].add(str(k))
                        col_check[col].add(str(k))
                        cube_check[(row // 3, col // 3)].add(str(k))
                        if backtracking(board):
                            return True
                        board[row][col] = '.'
                        row_check[row].remove(str(k))
                        col_check[col].remove(str(k))
                        cube_check[(row // 3, col // 3)].remove(str(k))
                    return False
            return True

        backtracking(board)


s = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)
