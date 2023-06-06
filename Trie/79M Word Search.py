from collections import Counter
from typing import List
"""
time complexity: O(4mn^k), mn:board, k:len(word)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        if len(word) > m * n:
            return False
        """
        optimization:
        """
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        if count[word[0]] > count[word[-1]]:
             word = word[::-1]

        def valid_neighbor(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True

        def dfs(i, j, index):
            if not valid_neighbor(i, j) or (i, j) in visited:
                return False
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            index += 1
            visited.add((i, j))
            res = dfs(i, j - 1, index) or dfs(i, j + 1, index) or dfs(i - 1, j, index) or dfs(i + 1, j, index)
            visited.remove((i, j))  # backtracking
            return res

        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
test = s.exist(board, word)
print(test)
