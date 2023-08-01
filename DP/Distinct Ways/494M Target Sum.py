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

    def findTargetSumWays_bottom_up(self, nums: List[int], target: int) -> int:
        # 假设这五个数中，加法的总和为x，减法的总和为sum - x
        # 在这种情况下，x - (sum - x) == target
        # so x == (sum + target) / 2
        total = sum(nums)
        if (total + target) % 2 == 1:
            return 0
        if total < target or -total > target:
            return 0
        dp_range = (total + target) // 2
        # 只算加法即可，即x的量。important
        table = [[0] * (dp_range + 1) for _ in range(len(nums) + 1)]
        table[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(dp_range + 1):
                # 不需要算减去的，因此只需要管与上面相同的或者加出来的
                table[i][j] += table[i - 1][j]
                if j - nums[i - 1] >= 0:
                    table[i][j] += table[i - 1][j - nums[i - 1]]
        return table[-1][-1]

    def findTargetSumWays_bottom_up2(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1:
            return 0
        if total < target or -total > target:
            return 0
        dp_range = (total + target) // 2
        table = [0] * (dp_range + 1)
        table[0] = 1
        for i in range(len(nums)):
            for j in range(dp_range, nums[i] - 1, -1):
                table[j] += table[j - nums[i]]
            # print(table)
        # print(table)
        return table[-1]


s = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
test = s.findTargetSumWays_bottom_up2(nums, target)
print(test)