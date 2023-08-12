import random
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quicksort(nums, start, end):
            if start >= end:
                return
            splitpointer = partition(nums, start, end)
            quicksort(nums, splitpointer + 1, end)
            quicksort(nums, start, splitpointer - 1)

        def partition(nums, start, end):
            x = random.randint(start, end)
            pivot = nums[x]
            nums[x], nums[start] = nums[start], nums[x]
            leftpointer = start + 1
            rightpointer = end
            while True:
                while leftpointer <= rightpointer and nums[leftpointer] <= pivot:
                    leftpointer += 1
                while leftpointer <= rightpointer and nums[rightpointer] >= pivot:
                    rightpointer -= 1
                if rightpointer < leftpointer:
                    break
                nums[leftpointer], nums[rightpointer] = nums[rightpointer], nums[leftpointer]
            nums[start], nums[rightpointer] = nums[rightpointer], nums[start]
            return rightpointer

        quicksort(nums, 0, len(nums) - 1)


s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)
