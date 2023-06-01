from typing import List
from collections import defaultdict

'''
Difficulty: Median
Solution: Use a hash map, key is the sorted string, value is the original string
Time complexity: O(nklogk), n * klogk + n, n is the length of input strs, k is the length of every word.
Space complexity: O(n), 2 * n, n is the length of input strs
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for str in strs:
            word = sorted(str)  # ['a', 'e', 't']
            key = ''.join(word)
            word_dict[key].append(str)
        ls = []
        for _ in word_dict:
            ls.append(word_dict[_])
        return ls


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = s.groupAnagrams(strs)
print(res)
