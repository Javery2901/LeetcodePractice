from typing import List


class Solution:
    def maxSubArray_sliding_window(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best_sum = nums[0]
        current_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
