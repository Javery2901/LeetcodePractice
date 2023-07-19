from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # sliding window
        # [2,1,1,2,1,4,3]
        # curr: 1,1,1,4,4,0,1
        start = 0
        count = 0
        curr = 0
        for end in range(len(nums)):
            if left <= nums[end] <= right:
                curr = end - start + 1
            elif nums[end] > right:
                curr = 0
                start = end + 1
            count += curr
        return count


s = Solution()
nums = [2,1,1,2,1,4,3]
left = 2
right = 3
test = s.numSubarrayBoundedMax(nums, left, right)
print(test)