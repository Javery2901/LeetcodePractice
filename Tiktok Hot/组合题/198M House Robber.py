from typing import List


class Solution:
    def rob_top_down(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dfs(n, memo):
            if n == 1:
                memo[n] = nums[n-1]
                return memo[n]
            if n == 2:
                memo[n] = max(nums[n - 1], nums[n - 2])
                return memo[n]
            if n in memo:
                return memo[n]
            memo[n] = max(dfs(n - 2, memo) + nums[n - 1], dfs(n - 1, memo))
            return memo[n]

        return dfs(n, memo)

    def rob_bottom_up(self, nums: List[int]) -> int:
        n = len(nums)
        table = [0] * (n + 1)  # [0, 0, 0, 0, 0]
        for i in range(1, n + 1):
            if i == 1:
                table[i] = max(table[i - 1], 0 + nums[i - 1])
            else:
                table[i] = max(table[i - 1], table[i - 2] + nums[i - 1])
        return table[-1]


    def rob_two_pointers(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, 0
        for i in range(1, n + 1):
            a, b = b, max(b, nums[i - 1] + a)
            print(a, b)
        return b


s = Solution()
nums = [2,7,9,3,1]
test = s.rob_bottom_up(nums)
print(test)