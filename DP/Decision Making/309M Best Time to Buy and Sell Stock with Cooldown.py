from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float('inf')

        for price in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            # Max profit of cooldown on Day i comes from
            # either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + price
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - price)

        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)

    def maxProfit_memo(self, prices: List[int]) -> int:

        # Bottom-up dynamic programming with memoization (caching)
        @lru_cache(None)
        def dp(day: int, can_buy: True) -> int:

            # Base case
            if day >= len(prices):
                return 0

            if can_buy:
                # We don't own any stocks. Two options:
                # 1. Don't buy any stocks and go to the next day (wait for a better opportunity)
                # 2. Buy stocks and go to the next day (with hope to have the best profit)
                return max(dp(day + 1, True), dp(day + 1, False) - prices[day])
            else:
                # We own stocks. Two options:
                # 1. Don't sell any stocks and go to the next day (maybe there is a better selling price)
                # 2. Sell the stocks and go to the day after tomorrow (cooldown tomorrow)
                return max(dp(day + 1, False), dp(day + 2, True) + prices[day])

        # Start with no stocks
        return dp(0, True)

    def maxProfit_bottom_up(self, prices: List[int]) -> int:
        # DP: 股票问题
        # 状态分析：对于第i天来说，有三种状态，持有/不持有/冷冻期
        # dp[i][0]表示第i天-持有-能够获得的最大利润
        # dp[i][1]表示第i天-不持有-能够获得的最大利润
        # dp[i][2]表示第i天-冷冻期-能够获得的最大利润

        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            # 如果第i天持有，可以是前一天继承而来的状态
            # 也可能是第i天新购买，那么前一天一定是冷冻期
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])

            # 如果第i天不持有股票，有可能是i天之前就已经不持有，即dp[i - 1][1]
            # 也有可能是第i天卖掉的，即dp[i - 1][0] + price[i]
            # 也有可能是继承冷冻期而来
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i], dp[i - 1][2])

            # 冷冻期可能是前一天就是冷冻期
            # 也可能是前一天处于不持有的状态
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])

        return max(dp[-1])


s = Solution()
prices = [1,2,3,0,2]
test = s.maxProfit(prices)
print(test)