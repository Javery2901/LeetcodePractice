"""
Runtime: ms56, beat 25%
Difficulty: Median
Solution: binary search
Time complexity: O(logn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[right]


sol = Solution()
nums = [11,13,15,17]
res = sol.findMin(nums)
print(res)
