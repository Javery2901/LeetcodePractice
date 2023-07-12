from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search, every time check if it is the peak number, if not,
        # go to the bigger side
        if len(nums) == 1:
            return nums[0]

        def bigger_direction(number):
            # if left side is bigger, return True, otherwise, return False
            if number == 0:
                return nums[number] > nums[number + 1]
            return nums[number - 1] > nums[number]

        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if bigger_direction(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1 if left > 0 else 0


s = Solution()
nums = [2,1]
test = s.findPeakElement(nums)
print(test)