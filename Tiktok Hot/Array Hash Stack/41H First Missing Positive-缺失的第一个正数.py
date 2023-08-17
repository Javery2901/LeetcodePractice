from typing import List
"""
Given an unsorted integer array nums, return the smallest missing positive integer.
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 缺失的数一定是[1,2,....n]之内的一个数
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1
            nums[val] = -abs(nums[val])  # 占位
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1


s = Solution()
nums = [1,1]
test = s.firstMissingPositive(nums)
print(test)

