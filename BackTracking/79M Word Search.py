from typing import List
from collections import Counter, defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count_word = Counter(word)
        count_board = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                count_board[board[i][j]] += 1
        for w in count_word:
            if count_word[w] > count_board[w]:
                return False

        if count_word[word[0]] > count_word[word[-1]]:
            word = word[::-1]

        def valid(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[i]):
                return True

        def backtracking(i, j, index):
            # print(i, j, index)
            if index == len(word):
                return True
            if not valid(i, j) or (i, j) in visited:
                return False
            if board[i][j] == word[index]:
                visited.add((i, j))
                if not (backtracking(i + 1, j, index + 1) or backtracking(i - 1, j, index + 1) or
                        backtracking(i, j + 1, index + 1) or backtracking(i, j - 1, index + 1)):
                    visited.remove((i, j))
                else:
                    return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # print(i, j, board[i][j])
                    visited = set()
                    if backtracking(i, j, 0):
                        return True
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
test = s.exist(board, word)
print(test)
