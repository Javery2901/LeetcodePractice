import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # try dfs
        stack = []
        print(stack)
        for i in range(len(board)):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][len(board[0]) - 1] == 'O':
                stack.append((i, len(board[0]) - 1))
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                stack.append((0, i))
            if board[len(board) - 1][i] == 'O':
                stack.append((len(board) - 1, i))

        visited = set()

        def valid(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return True

        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            for x, y in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                if valid(x,y) and board[x][y] == 'O' and (x, y) not in visited:
                    stack.append((x, y))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    print(i, j)
                    if (i, j) not in visited:
                        board[i][j] = 'X'


s = Solution()
board = [["X","X","X"],["X","O","X"],["X","X","X"]]
s.solve(board)
print(board)
