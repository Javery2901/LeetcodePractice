import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_words(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.flag = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])
        """
        words list optimization: if the length of word is larger than the board size
        we can neglect the word.
        if the number of any letter in the word is larger than the number of the letter in the board
        we can neglect the word
        ["oath","pea","eat","rain"] -> ['oath', 'eat', 'rain']
        time complexity: O(len(words) * len(word)) 3 * 10^5
        """
        count = collections.Counter(sum(board, []))
        trie = Trie()
        for word in words:
            if len(word) <= m * n:
                add = True
                for char, count_word in collections.Counter(word).items():
                    if count[char] < count_word:
                        add = False
                        break
                if add:
                    trie.add_words(word)

        def valid_neighbor(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True

        def dfs(i, j, node, path):
            if node.flag:
                res.add(path)
                if not node.children:
                    return True

            if node.children:
                for rr, cc in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                    if valid_neighbor(rr, cc):
                        letter = board[rr][cc]
                        if (rr, cc) not in visited and letter in node.children:
                            visited.add((rr, cc))
                            if dfs(rr, cc, node.children[letter], path + letter):
                                del node.children[letter]
                            visited.remove((rr, cc))
            return len(node.children) == 0

        res = set()
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter in trie.root.children:
                    visited = {(i, j)}
                    dfs(i, j, trie.root.children[letter], letter)
        return list(res)


s = Solution()
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
test = s.findWords(board, words)
print(test)