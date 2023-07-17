from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        # left is even, right is odd
        while left < len(nums) and right > 0:
            while left < len(nums) and nums[left] % 2 == 0:
                left += 2
            while right > 0 and nums[right] % 2 == 1:
                right -= 2
            if left < len(nums) and right > 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 2
                right -= 2
        return nums


s = Solution()
nums = [2, 3]
test = s.sortArrayByParityII(nums)
print(test)
