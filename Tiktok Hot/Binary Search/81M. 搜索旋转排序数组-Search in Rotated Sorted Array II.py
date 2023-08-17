from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 最左和最右如果有相同元素，左边的忽略
        left, right = 0, len(nums) - 1
        while left < len(nums) and nums[left] == nums[right]:
            left += 1
        if left == len(nums):
            return nums[right] == target

        # 接下来与leetcode33相同
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # 判断mid和左的关系
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # nums[mid] < nums[left]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left] == target


s = Solution()
nums = [1,3]
target = 3
test = s.search(nums, target)
print(test)