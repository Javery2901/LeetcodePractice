import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        counter_p = collections.Counter(p)
        counter_s = collections.Counter(s[0: len(p)])
        if counter_s == counter_p:
            res.append(0)
        left = 0
        for right in range(len(p), len(s)):
            if counter_s[s[left]] == 1:
                del counter_s[s[left]]
            else:
                counter_s[s[left]] -= 1
            counter_s[s[right]] += 1

            if counter_s == counter_p:
                res.append(left + 1)
            left += 1
        return res







so = Solution()
s = "cbaebabacd"
p = "abc"
test = so.findAnagrams(s, p)
print(test)
