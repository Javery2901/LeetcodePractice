"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(26 * n)
Space complexity: O(26)
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_element = 0
        ret = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_element = max(max_element, count[s[right]])
            if right - left + 1 - max_element > k:
                count[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret


sol = Solution()
s = "AABABBA"
k = 1
res = sol.characterReplacement(s, k)
print(res)
