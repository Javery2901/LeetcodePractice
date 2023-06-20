"""
Difficulty: Easy
Solution: Sliding Window, go from left to right, find the min left, update the max profit
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        change = False
        left = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if left > prices[i]:
                left = prices[i]
                change = True
            if not change and max_profit < prices[i] - left:
                max_profit = prices[i] - left
            change = False
        return max_profit

    def maxProfit_template(self, prices: List[int]) -> int:  # 也是贪心的思路
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
res = sol.maxProfit_template(prices)
print(res)
