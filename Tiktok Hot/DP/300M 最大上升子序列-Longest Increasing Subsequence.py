from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(table[i], table[j] + 1)
        return max(table)
