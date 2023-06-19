from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        best_index = 0
        prev_best_index = 0
        jump = 0

        for index, num in enumerate(nums):
            if index + num > best_index:
                best_index = index + num

            if index == prev_best_index:
                jump += 1
                prev_best_index = best_index
                if prev_best_index >= len(nums) - 1:
                    return jump


s = Solution()
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
test = s.jump(nums)
print(test)