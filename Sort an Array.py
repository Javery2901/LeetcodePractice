import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:  # if array is already sorted, n2
        def quicksort_helper(nums, start, end):
            if start >= end:
                return
            splitpointer = partition(nums, start, end)
            quicksort_helper(nums, start, splitpointer - 1)
            quicksort_helper(nums, splitpointer + 1, end)

        def partition(nums, start, end):
            pivot = nums[start]  # go from ls[0]
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

        quicksort_helper(nums, 0, len(nums) - 1)
        return nums

    def sortArray_random(self, nums: List[int]) -> List[int]:  # if all elements are the same, n2
        def quicksort_helper(nums, start, end):
            if start >= end:
                return
            splitpointer = partition(nums, start, end)
            quicksort_helper(nums, start, splitpointer - 1)
            quicksort_helper(nums, splitpointer + 1, end)

        def partition(nums, start, end):
            x = random.randint(start, end)
            pivot = nums[x]  # random
            nums[start], nums[x] = nums[x], nums[start]
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

        quicksort_helper(nums, 0, len(nums) - 1)
        return nums

    def sortArray_merge(self, nums: List[int]) -> List[int]:  # if all elements are the same, n2

        def mergesort_helper(left, right):
            merge = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merge.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    merge.append(right[j])
                    j += 1
            for x in range(i, len(left)):
                merge.append(left[x])
            for y in range(j, len(right)):
                merge.append(right[y])
            return merge

        def mergesort(nums):
            if len(nums) == 1:
                return nums
            middle = len(nums) // 2
            left = mergesort(nums[:middle])
            right = mergesort(nums[middle:])
            return mergesort_helper(left, right)

        return mergesort(nums)


s = Solution()
nums = [-2,3,-5]
test = s.sortArray_merge(nums)
print(test)