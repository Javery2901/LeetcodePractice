"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        min_len = float('inf')  # 找最大值，就赋给他最小初始值。
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:  # 有些题是if，根据题目需要确定
                # 在这道题中，通过while来确定加法是否大于target
                # 在这道题中，不需要考虑right回缩
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]  # 本质是在缩小滑动窗口，窗口内容也需更新
                left += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len


sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
res = sol.minSubArrayLen(target, nums)
print(res)