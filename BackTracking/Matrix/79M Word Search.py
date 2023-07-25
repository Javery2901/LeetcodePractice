import collections
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        counter_word = collections.Counter(word)
        counter_board = collections.defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[i])):
                counter_board[board[i][j]] += 1
        for w in counter_word:
            if w not in counter_board or counter_word[w] > counter_board[w]:
                return False
        if counter_board[word[0]] > counter_board[word[-1]]:
            word = word[::-1]
        print(word)

        def valid(r, c):
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                return True
            return False

        def backtracking(row, col, index):

            if index == len(word):
                return True
            for r, c in ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)):
                if not valid(r, c) or (r, c) in visited or board[r][c] != word[index]:
                    continue
                # now this point is not in visited, is the right word in the board
                print(row, col, r, c)
                visited.add((r, c))
                if backtracking(r, c, index + 1):
                    return True
                visited.remove((r,c))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    if backtracking(i, j, 1):
                        return True
        return False


s = Solution()
board = [["A","A","A"],["A","a","a"],["A","a","A"],["a","a","A"]]
word = "AAAAAA"
test = s.exist(board, word)
print(test)
