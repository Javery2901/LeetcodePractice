from math import inf
from typing import List


class Solution:
    def maxSubArray_sliding_window2(self, nums: List[int]) -> int:  # fast
        if len(nums) == 1:
            return nums[0]
        left = 0
        current_max = 0
        best_max = -inf
        for right in range(len(nums)):
            current_max += nums[right]
            best_max = max(best_max, current_max)
            while current_max < 0:  # important, 处理left指针问题
                # 当current_sum < 0, 代表subarray的起始点开始移动，即left收缩窗口直到当current_sum 回归0
                current_max -= nums[left]
                left += 1
        return best_max


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = s.maxSubArray_sliding_window2(nums)
print(test)

