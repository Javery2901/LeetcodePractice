"""
Difficulty: Hard
Solution: binary search template
Time complexity: O(nlogs)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(capacity):
            splits = 1
            count = 0
            for i in nums:
                count += i
                if count > capacity:
                    count = i
                    splits += 1
                    if splits > k:
                        return False
            return True

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
nums = [1,2,3,4,5]
k = 2
res = sol.splitArray(nums, k)
print(res)