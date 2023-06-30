from typing import List


class Solution:
    def canPartition_brutal_top_down(self, nums: List[int]) -> bool:
        # S1 + S2 = sum, S1 - S2 = 0 --> S1 == S2 == sum // 2
        if sum(nums) % 2 != 0 or len(nums) == 1:
            return False
        target = sum(nums) // 2
        memo = {}

        def recursion(index, cur_value):
            if cur_value == 0:
                return True
            if index == len(nums):
                return False
            if (index, cur_value) in memo:
                return memo[(index, cur_value)]
            memo[(index, cur_value)] = recursion(index + 1, cur_value) or recursion(index + 1, cur_value - nums[index])
            return memo[(index, cur_value)]

        recursion(0, target)
        # print(memo)
        return memo[(0, target)]

    def canPartition_brutal_bottom_up(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 or len(nums) == 1:
            return False
        target = sum(nums) // 2  # target will not be 0
        table = set()
        table.add(0)

        for i in range(len(nums)):
            temp_table = set()
            for t in table:
                curr = t + nums[i]
                if curr == target:
                    return True
                temp_table.add(curr)
                temp_table.add(t)
            table = temp_table
        return True if target in table else False


s = Solution()
nums = [14,9,8,4,3,2]
test = s.canPartition_brutal_bottom_up(nums)
print(test)
