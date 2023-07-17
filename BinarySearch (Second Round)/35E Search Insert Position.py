from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return left
        # left is the minimum requirement


s = Solution()
nums = [1,3,5,6]
target = 2
test = s.searchInsert(nums, target)
print(test)
