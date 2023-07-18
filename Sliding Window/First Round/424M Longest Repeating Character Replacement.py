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
        left = 0  # left side of the window
        right = 0  # right side of the window
        max_count = 0
        for i in range(len(s)):
            heuristic[s[i]] += 1  # update the number of s[i]
            right += 1
            cells_count = right - left  # cells_count: the number in the window
            if cells_count - max(heuristic.values()) <= k:
                max_count = max(max_count, cells_count)
            else:
                heuristic[s[left]] -= 1
                left += 1
            # cells_count - max(heuristic.values()) <= k,
            # it means that cells_count can contain the same latter within k changes
            # otherwise, the left side of the window should + 1
            # and the number of s[left] in the heuristic should - 1
        return max_count


sol = Solution()
s = "AABABBA"
k = 1
res = sol.characterReplacement(s, k)
print(res)
