from cmath import inf
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
        # 随想录系列

        table = [[0] * 2 for _ in range(len(prices))]
        # table[i][0] 代表持有股票时手头的总金额， table[i][1] 代表手头不持有股票时的总金额
        table[0][0] = -prices[0]
        table[0][1] = 0
        for i in range(1, len(prices)):
            table[i][0] = max(table[i - 1][0], -prices[i])
            # (跟前一天一样继续持有时现金总额，或者花现金买入后的现金总额)
            table[i][1] = max(table[i - 1][1], table[i - 1][0] + prices[i])
            # （跟前一天一样继续不持有时现金总额，或者将昨天持有的卖出后的现金总额）
        print(table)
        return table[-1][-1]


s = Solution()
prices = [7,1,5,3,6,4]
test = s.maxProfit_bottom_up(prices)
print(test)