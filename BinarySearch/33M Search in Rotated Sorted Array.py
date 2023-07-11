from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first check if the target is in larger subarray or smaller subarray
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:  # target is in larger subarray
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 3
test = s.search(nums, target)
print(test)