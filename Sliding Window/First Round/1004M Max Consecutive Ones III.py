"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        max_element = 0
        left = 0
        ret = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            max_element = max(max_element, count[1])
            if right - left + 1 - max_element > k:
                count[nums[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret


sol = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
res = sol.longestOnes(nums, k)
print(res)
