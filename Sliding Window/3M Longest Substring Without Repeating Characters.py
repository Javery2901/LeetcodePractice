"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        heuristic = defaultdict(int)
        left = 0  # update the left word
        right = 0  # update the right word
        max_count = 0
        for i in range(len(s)):
            if s[i] in heuristic:
                max_count = max(max_count, i - left)
                if left <= heuristic[s[i]]:
                    left = heuristic[s[i]] + 1  # update left pointer, update max_count
            right += 1
            heuristic[s[i]] = i
            print(left, right)
            print(heuristic)
        max_count = max(max_count, right - left)
        return max_count


sol = Solution()
s = "abba"
res = sol.lengthOfLongestSubstring(s)
print(res)