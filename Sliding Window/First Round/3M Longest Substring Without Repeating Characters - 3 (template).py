"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        known = defaultdict(int)
        left = 0
        right = 0
        max_len = -float('inf')
        for right in range(len(s)):
            if s[right] in known:
                # 如果出现重复字母，则记录一次max_len， 且更新left位置，left重复字母的最大位置的右边一位
                max_len = max(max_len, right - left)
                left = max(left, known[s[right]] + 1)
            known[s[right]] = right  # 记录s[right]的当前位置

        if s:
            right += 1  # 若s存在，则说明循环结束，right应该加一位，从而计算一个最终值right - left
        max_len = max(max_len, right - left)
        return max_len


sol = Solution()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)
