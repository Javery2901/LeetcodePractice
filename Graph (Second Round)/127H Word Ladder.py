import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # use bfs, 每次将beginword的词上下扩展，寻找这里有哪些在wordlist中
        # 这些将作为neighbor word被添加到下一轮，一直到找不到或者找到为止

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        def bfs(word):
            res = []
            for i in range(len(word)):
                for j in range(97, 123):
                    neighbor = word[: i] + chr(j) + word[i + 1:]
                    if neighbor == word:
                        continue
                    if neighbor in word_set:
                        res.append(neighbor)
            return res

        res = 0
        visited = {beginWord}
        queue = collections.deque([beginWord])
        while queue:
            # print(queue, res)
            # print(visited)
            res += 1
            for _ in range(len(queue)):
                pop_word = queue.popleft()
                if pop_word == endWord:
                    return res
                neighbor_list = bfs(pop_word)
                # print(neighbor_list)
                for neighbor in neighbor_list:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        if not queue:
            return 0


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(s.ladderLength(beginWord, endWord, wordList))