from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [[0] * len(prices) for _ in range(3)]
        """
          1 2 4 2 5 7 2 4 9  8
        0 0 0 0 0 0 0 0 0 0  0 
        1 0 1 3 3 4 6 6 6 8  8 
        2 0 1 3 3 6 8 8 8 13 13
        """
        for i in range(1, 3):
            buy = prices[0]
            for j in range(1, len(prices)):
                table[i][j] = max(table[i][j - 1], prices[j] - buy)
                buy = min(buy, prices[j] - table[i - 1][j - 1])
                # print(prices[j], buy)
        print(table)
        return table[-1][-1]

    def maxProfit_bottom_up(self, prices: List[int]) -> int:
        # 随想录系列
        """
        用5行表示每天的动作：
        table[i][0]: 不做操作时手头现金总额 table[i][0] = table[i - 1][0]
        table[i][1]: 第一次持有的手头现金总额  table[i][1] = max(table[i - 1][1], table[i - 1][0] - prices[i])
                     (跟昨天一样继续持有时的手头现金总额，昨天没操作的情况下今天买入后的手头现金总额)
        table[i][2]: 第一次不持有的手头现金总额  table[i][2] = max(table[i - 1][2], table[i - 1][1] + prices[i])
                     (跟昨天一样继续不持有时的手头现金总额，昨天持有情况下今天卖出后的手头现金总额)
        table[i][3]: 第二次持有的手头现金总额  table[i][3] = max(table[i - 1][3], table[i - 1][2] - prices[i])
                     (跟昨天一样继续持有时的手头现金总额，昨天第一次卖出股票的情况下今天买入后的手头现金总额)
        table[i][4]: 第二次不持有的手头现金总额  table[i][4] = max(table[i - 1][4], table[i - 1][3] + prices[i])
                     (跟昨天一样继续不持有时的手头现金总额，昨天第二次持有情况下今天卖出后的手头现金总额)
        """
        table = [[0] * 5 for _ in range(len(prices))]
        table[0][0], table[0][1], table[0][2], table[0][3], table[0][4] = 0, -prices[0], 0, -prices[0], 0
        # 可看作是第一天买入卖出买入卖出
        for i in range(1, len(prices)):
            table[i][0] = table[i - 1][0]
            table[i][1] = max(table[i - 1][1], table[i - 1][0] - prices[i])
            table[i][2] = max(table[i - 1][2], table[i - 1][1] + prices[i])
            table[i][3] = max(table[i - 1][3], table[i - 1][2] - prices[i])
            table[i][4] = max(table[i - 1][4], table[i - 1][3] + prices[i])
        # print(table)
        return table[-1][-1]


    def maxProfit_greedy(self, prices: List[int]) -> int:
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            print(buy1, profit1)
            print(buy2, profit2)
            print()
        return profit2


s = Solution()
prices = [3,3,5,0,0,3,1,4]
test = s.maxProfit_bottom_up(prices)
print(test)
