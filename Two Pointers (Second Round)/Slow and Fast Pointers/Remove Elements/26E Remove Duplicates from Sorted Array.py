from cmath import inf
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = -inf
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != unique:
                unique = nums[fast]
                nums[slow] = nums[fast]
                slow += 1
        return slow
