from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # O(len(dictionary) * len(dictionary[i]))
        res = ''
        for word in dictionary:
            i = j = 0
            # two pointers
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word): # means word is in s
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res


so = Solution()
s = "abce"
dictionary = ["abe","abc"]
test = so.findLongestWord(s, dictionary)
print(test)