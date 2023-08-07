from cmath import inf
from typing import List


class Solution:
    def maxSubArray_two_pointers(self, nums: List[int]) -> int:
        left = 0
        current_max = 0
        best_max = -inf
        for right in range(len(nums)):
            current_max += nums[right]
            best_max = max(best_max, current_max)
            while current_max < 0:
                current_max -= nums[left]
                left += 1
        return best_max

    def maxSubArray_greedy(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best_sum = nums[0]
        current_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum

    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)  # at first dp[-1] == 0
        print(dp)
        return max(dp)

    def maxSubArray_top_down(self, nums):

        dp = [0] * len(nums)

        def recursion(index):
            if index == 0:
                dp[index] = nums[0]
            else:
                dp[index] = max(nums[index], recursion(index - 1) + nums[index])
            return dp[index]

        recursion(len(nums) - 1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray_top_down(nums))
