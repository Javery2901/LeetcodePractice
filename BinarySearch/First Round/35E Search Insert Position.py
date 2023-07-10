"""
Difficulty: Easy
Solution: binary search template
Time complexity: O(logn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
            print(left, right)
        return left  # left is the minimum k that satisfies nums[mid] >= target


sol = Solution()
nums = [3,6,7,11]
target = 8
res = sol.searchInsert(nums, target)
print(res)