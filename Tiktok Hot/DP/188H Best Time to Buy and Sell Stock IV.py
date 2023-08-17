from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        table = [[0] * len(prices) for _ in range(k + 1)]

        for i in range(1, k + 1):
            buy = prices[0]
            for j in range(1, len(prices)):
                table[i][j] = max(table[i][j - 1], prices[j] - buy)  # do nothing, or sell
                buy = min(buy, prices[j] - table[i - 1][j - 1])  # buy: we hold , or update buy
                # table[i - 1][j - 1] means we complete a transaction yesterday,
                # prices[j] - table[i - 1][j - 1] means we buy new stock today, this can be < 0
        return table[-1][-1]

    def maxProfit_bottom_up(self, k: int, prices: List[int]) -> int:
        # 随想录系列
        # 本质上把2次改变为k次。
        table = [[0] * (2 * k + 1) for _ in range(len(prices))]
        """
        table[i][0] 第一列代表不做任何操作
        table[i][j] 代表第j轮持有股票时的手头金额，max(与昨天相同的，第j-1轮卖出后重新买入的手头金额)
        table[i][j + 1] 代表第j轮不持有股票的手头金额，max(与昨天相同的，昨天持有今天卖出后的手头金额)
        """
        for j in range(1, 2 * k, 2):
            table[0][j] = -prices[0]
        # table[0] = [0, -prices[0], 0, -prices[0], ......]

        for i in range(1, len(prices)):  # 从列表中的第二个数开始，第一个数已经被初始化
            for j in range(1, 2 * k, 2):  # 2次时，j取值1，3
                table[i][j] = max(table[i - 1][j], table[i - 1][j - 1] - prices[i])
                table[i][j + 1] = max(table[i - 1][j + 1], table[i - 1][j] + prices[i])
        print(table)




s = Solution()
k = 2
prices = [3,2,6,5,0,3]
test = s.maxProfit_bottom_up(k, prices)
print(test)