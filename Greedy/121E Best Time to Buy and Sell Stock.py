from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            max_profit = max(max_profit, prices[i] - buy)
        return max_profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
res = sol.maxProfit(prices)
print(res)