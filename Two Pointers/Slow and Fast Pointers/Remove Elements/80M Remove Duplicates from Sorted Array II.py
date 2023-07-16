from cmath import inf
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:  # this is the first one, no problem
                count = 1
            else:
                count += 1
            if count < 3:  # only if count < 3, slow changes, otherwise, slow remains
                nums[slow] = nums[fast]
                slow += 1
        return slow


s = Solution()
nums = [0,0,1,1,1,1,2,3,3]
s.removeDuplicates(nums)
print(nums)