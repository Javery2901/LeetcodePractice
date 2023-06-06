import collections
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # words_set = set(words)  # {'w', 'wo', 'wor', 'worl', 'world'}
        # adict = collections.defaultdict(list)
        # for word in words:  # O(n)
        #     freq = 0
        #     for i in range(1, len(word) + 1):  # O(k)
        #         if word[: i] in words_set:  # O(k) 30 * 30 * 1000 = 900000
        #             freq += 1
        #         else:
        #             break
        #     adict[freq].append(word)
        # max_freq = max(adict)
        # if max_freq == 0:
        #     return ''
        # return min(adict[max_freq])

        """
        optimal
        """
        words.sort()
        words_set = set()
        res = ''
        for word in words:
            if len(word) == 1 or word[:-1] in words_set:
                res = word if len(word) > len(res) else res
                words_set.add(word)
        return res


words = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
s = Solution()
test = s.longestWord(words)
print(test)