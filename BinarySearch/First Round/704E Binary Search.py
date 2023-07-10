"""
Time complexity: O(logn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1





sol = Solution()
nums = [5]
target = 5
res = sol.search(nums, target)
print(res)