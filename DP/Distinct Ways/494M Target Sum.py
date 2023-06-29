from typing import List


class Solution:
    def findTargetSumWays_top_down(self, nums: List[int], target: int) -> int:
        memo = {}  # ()index, total) -> # of ways

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in memo:
                return memo[(index, total)]
            memo[(index, total)] = dfs(index + 1, total - nums[index]) + dfs(index + 1, total + nums[index])
            return memo[(index, total)]

        dfs(0, 0)
        # print(memo)
        return memo[(0, 0)]


s = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
test = s.findTargetSumWays_top_down(nums, target)
print(test)