from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1] * len(nums)
        for i in range(len(nums) - 1, - 1, -1):  # 遍历背包
            for j in range(i + 1, len(nums)):  # 遍历物品
                if nums[i] < nums[j]:
                    table[i] = max(table[i], table[j] + 1)
            # print(table)
        return max(table)

    def lengthOfLIS_bottom_Up(self, nums: List[int]) -> int:
        # 代码随想录
        table = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(table[j] + 1, table[i])
        return max(table)


s = Solution()
nums = [4,10,4,3,8,9]
print(s.lengthOfLIS_bottom_Up(nums))