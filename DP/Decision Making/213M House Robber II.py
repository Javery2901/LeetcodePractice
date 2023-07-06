from typing import List

"""
其实可以看作两个nums，一个去掉第一个数，一个去掉最后一个数
原因：任何情况下都不可能出现第一个数和最后一个数同时出现的情况，对中间过程来讲，如果它用到了第一个数，那么它不可能传导到最后一个数上
"""


class Solution:

    def rob_bottom_up(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums) - 1
        table_without_index_first = [0] * (n + 2)  # will only contain information nums[1:]
        table_without_index_first[2:] = nums[1:]
        table_without_index_last = [0] * (n + 2)  # will only contain information nums[:-1]
        table_without_index_last[2:] = nums[:-1]
        for i in range(2, n + 2):
            table_without_index_first[i] = max(table_without_index_first[i] + table_without_index_first[i - 2],
                                               table_without_index_first[i - 1])
            table_without_index_last[i] = max(table_without_index_last[i] + table_without_index_last[i - 2],
                                              table_without_index_last[i - 1])
        print(table_without_index_first, table_without_index_last)
        return max(table_without_index_first[n+1], table_without_index_last[n+1])

    def rob_top_down(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def recursion(index, ls, memo):
            if index == 0:
                return ls[0]
            if index == 1:
                return max(ls[0], ls[1])
            if index in memo:
                return memo[index]
            memo[index] = max(recursion(index - 1, ls, memo), recursion(index - 2, ls, memo) + ls[index])
            return memo[index]

        return max(recursion(n - 2, nums[:-1], {}), recursion(n - 2, nums[1:], {}))

    def rob_two_pointer(self, nums: List[int]) -> int:

        def dfs(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + 1, rob2)
            return rob2

        return max(nums[0], dfs(nums[1:]), dfs(nums[:-1]))


s = Solution()
nums = [1,2,3]
test = s.rob_top_down(nums)
print(test)
