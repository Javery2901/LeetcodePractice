from typing import List


class Solution:
    def combinationSum4_backtrack(self, nums: List[int], target: int) -> int:
        # TLE
        # nums = [4,2,1] target = 32
        nums.sort()
        res = [0]
        if target < nums[0]:
            return 0

        def backtrack(target):
            if target < 0:
                return
            if target == 0:
                res[0] += 1
                return
            for i in range(len(nums)):
                backtrack(target - nums[i])

        backtrack(target)
        return res[0]

    def combinationSum4_bottom_up(self, nums: List[int], target: int) -> int:
        # important note: nums = [1,2,4] target = 10
        # table[10] = table[9] + table[8] + table[6]

        table = [0] * (target + 1)
        table[0] = 1
        for i in range(target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    table[i] += table[i - nums[j]]
        return table[-1]

    def combinationSum4_top_down(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(t, memo):
            if t in memo:
                return memo[t]
            if t == 0:
                return 1
            if t < 0:
                return 0
            res = 0
            for i in nums:
                res += dfs(t-i, memo)
            memo[t] = res
            return memo[t]

        dfs(target, memo)
        return memo[target]


s = Solution()
nums = [1,2,3]
target = 4
test = s.combinationSum4_bottom_up(nums, target)
print(test)