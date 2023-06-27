from cmath import inf
from typing import List


class Solution:
    def minCostClimbingStairs_top_down(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)

        def dfs(n, memo):
            if n <= 1:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(dfs(n-1, memo) + cost[n-1], dfs(n-2, memo) + cost[n-2])
            return memo[n]
        return dfs(n, memo)

    def minCostClimbingStairs_bottom_up(self, cost: List[int]) -> int:
        n = len(cost)
        table = [0] * (n + 1)
        for i in range(2, n + 1):
            table[i] = min(table[i - 1] + cost[i - 1], table[i - 2] + cost[i - 2])
        return table[n]

    def minCostClimbingStairs_two_pointer(self, cost: List[int]) -> int:
        a = 0
        b = 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(a + cost[i - 2], b + cost[i - 1])
        return b

s = Solution()
cost = [10,15,20]
test = s.minCostClimbingStairs_two_pointer(cost)
print(test)