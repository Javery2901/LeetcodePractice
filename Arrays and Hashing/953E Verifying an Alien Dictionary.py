from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, e in enumerate(order):
            dic[e] = i + 1
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if dic[word1[j]] == dic[word2[j]]:
                    continue
                elif dic[word1[j]] > dic[word2[j]]:
                    return False
                else:
                    break
        return True
