from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [0] * len(prices)
        for i in range(1, len(prices)):
            table[i] = max(0, prices[i] - prices[i - 1]) + table[i - 1]
        return table[-1]

    def maxProfit_bottom_up(self, prices: List[int]) -> int:
        # 随想录系列

        table = [[0] * 2 for _ in range(len(prices))]
        """
        table[i][0] 表示在第i天持有股票的手头现金总额，
        table[i][0] = max(table[i - 1][0], -prices[i]) 
        （跟昨天同样继续持股时的手头现金总额， 今天重新买入后的手头现金总额(其等于昨天不持股时的现金总金额减去今天要买的股票的成本)）
        table[i][1] = max(table[i - 1][1], table[i - 1][0] + prices[i])
        (跟昨天同样继续不持股时的手头现金总额，今天卖出后的手头现金总额)
        """
        table[0][0] = -prices[0]
        table[0][1] = 0
        for i in range(1, len(prices)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1] - prices[i])
            table[i][1] = max(table[i - 1][1], table[i - 1][0] + prices[i])
        print(table)
        return table[-1][-1]


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit_bottom_up(prices))