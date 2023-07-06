from typing import List


class Solution:
    def maxProfit_sliding_window(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit

    def maxProfit_greedy(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            max_profit = max(max_profit, prices[i] - buy)
        return max_profit

    def maxProfit_bottom_up(self, prices: List[int]) -> int:
        table = [0] * (len(prices))
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            table[i] = max(table[i - 1], prices[i] - buy)
        return table[-1]


s = Solution()
prices = [7,1,5,3,6,4]
test = s.maxProfit_bottom_up(prices)
print(test)