from typing import List


class Solution:
    def rotate_slice(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        nums[:] = nums[-step:] + nums[:-step]

    def rotate_two_pointers(self, nums: List[int], k: int) -> None:
        step = k % len(nums)

        def two_pointer_reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        two_pointer_reverse(0, len(nums) - 1)
        two_pointer_reverse(0, k - 1)
        two_pointer_reverse(k, len(nums) - 1)


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s.rotate_two_pointers(nums, k)
print(nums)
