import collections
from typing import List
from collections import defaultdict

'''
Difficulty: Median
Solution: Use one hash table to record and check if the sudoku is valid
Time complexity: O(n2) n is the length of sudoku, optimal solution
Space complexity: O(n2) n is the length of sudoku, optimal solution
Analysis: This is the optimal solution.
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_dict = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    continue
                if num in board_dict:
                    for element in board_dict[num]:
                        if (element[0] == i) or (element[1] == j) or (
                                element[0] // 3 == i // 3 and element[1] // 3 == j // 3):
                            return False
                board_dict[num].append((i, j))
        return True

    def isValidSudoku_0811(self, board: List[List[str]]) -> bool:
        # check row:
        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

        # check col:
        for i in range(len(board)):
            col_set = set()
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])

        # group check
        group_dic = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in group_dic[(i // 3, j // 3)]:
                    return False
                group_dic[(i // 3, j // 3)].add(board[i][j])

        return True


s = Solution()
board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
res = s.isValidSudoku_0811(board)
print(res)
