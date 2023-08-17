from typing import List
"""
给你一个可能存在 重复 元素值的数组 nums ，
它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 有重复值，先判断是否被截断成左右两边
        # 若没有，按照二分法正常进行
        # 若有，指针忽略左边的

        def binary_search(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return nums[left]

        if len(nums) == 1:
            return nums[0]
        if nums[0] == nums[-1]:  # eg [3,4,4,4,4,4,4,4,0,1,2,3,3,3,3]
            left, right = 1, len(nums) - 1
            while left < len(nums) and nums[left] == nums[left - 1]:
                left += 1
            if left == len(nums):
                return nums[right]
        else:
            left, right = 0, len(nums) - 1
        return binary_search(left, right)


s = Solution()
# nums = [3,4,4,4,4,4,4,4,1,2,3,3,3,3]
nums = [2,2,2,0,1]
test = s.findMin(nums)
print(test)



