"""
Difficulty: Medium
Solution: Sliding Window, fixed window size
Time complexity: O()
Space complexity: O()
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        template = Counter(s1)
        for right in range(len(s1) - 1, len(s2)):
            # check if the substring in window is one type of s1's permutation
            # to do this, the best way is to use hash table
            if Counter(s2[left: right + 1]) == template:
                return True
            else:
                left += 1
        return False


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = sol.checkInclusion(s1, s2)
print(res)
