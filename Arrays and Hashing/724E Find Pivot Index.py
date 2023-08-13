from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        left_side = sum(nums[:pivot])
        right_side = sum(nums[pivot + 1:])
        print(left_side, right_side)
        while pivot < len(nums) - 1:
            if left_side == right_side:
                return pivot
            left_side += nums[pivot]
            right_side -= nums[pivot + 1]
            pivot += 1
            print(left_side, right_side, pivot)

        if left_side == right_side:
            return pivot
        return -1


s = Solution()
nums = [1,2,3]
print(s.pivotIndex(nums))