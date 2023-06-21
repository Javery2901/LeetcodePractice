from math import inf
from typing import List
"""
数学逻辑：在一个环的list中，如果说我们找到了一个subarray，其和为最大和，那么其余部分的和必为最小和
解释：一个list的sum是固定的，当找到了最大和时，其余的必为最小和。

"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = 0
        best_max = -inf
        current_min = 0
        best_min = inf
        for i in range(len(nums)):
            x = nums[i]
            current_max = max(x, x + current_max)
            best_max = max(best_max, current_max)
            current_min = min(x, x + current_min)
            best_min = min(best_min, current_min)
        print(best_max)
        print(best_min)
        return best_max if best_max < 0 else max(best_max, sum(nums) - best_min)


s = Solution()
nums = [-3,-2,-3]
test = s.maxSubarraySumCircular(nums)
print(test)
