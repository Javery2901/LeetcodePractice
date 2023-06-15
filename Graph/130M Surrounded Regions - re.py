from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()

        def valid(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return True

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for x, y in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                if valid(x, y) and board[x][y] == 'O':
                    dfs(x, y, visited)

        for i in range(len(board)):
            if board[i][0] == 'O' and (i, 0) not in visited:
                dfs(i, 0, visited)
            if board[i][len(board[0]) - 1] == 'O' and (i, len(board[0]) - 1) not in visited:
                dfs(i, len(board[0]) - 1, visited)

        for i in range(len(board[0])):
            if board[0][i] == 'O' and (0, i) not in visited:
                dfs(0, i, visited)
            if board[len(board) - 1][i] == 'O' and (len(board) - 1, i) not in visited:
                dfs(len(board) - 1, i, visited)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'



s = Solution()
board = [["O"]]
s.solve(board)
print(board)