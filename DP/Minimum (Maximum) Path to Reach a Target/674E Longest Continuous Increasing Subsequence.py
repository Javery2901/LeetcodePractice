from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_res = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            max_res = max(max_res, count)
        return max_res

    def findLengthOfLCIS_bottom_up(self, nums: List[int]) -> int:
        table = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                table[i] = table[i + 1]
        return max(table)


s = Solution()
nums = [1,3,5,4,7]
test = s.findLengthOfLCIS(nums)
print(test)