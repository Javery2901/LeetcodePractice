"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(26 * n)
Space complexity: O(26)
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        heuristic = defaultdict(int)
        max_count = 0
        for i, e in enumerate(s):
            heuristic[e] += 1
            if max_count + 1 - max(heuristic.values()) <= k:
                max_count += 1
            else:
                heuristic[s[i - max_count]] -= 1
        return max_count


sol = Solution()
s = "AABABBA"
k = 1
res = sol.characterReplacement(s, k)
print(res)
