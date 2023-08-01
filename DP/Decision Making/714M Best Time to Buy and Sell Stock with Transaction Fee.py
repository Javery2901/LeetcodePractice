from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 代码随想录
        table = [[0] * 2 for _ in range(len(prices))]
        table[0][0] = - prices[0]
        for i in range(1, len(prices)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1] - prices[i])
            table[i][1] = max(table[i - 1][1], table[i - 1][0] + prices[i] - fee)
            # 卖出时需要付一笔手续费，从而查看是否有必要卖出盈利
        # print(table)
        # if fee = 0, [[-1, 0], [-1, 2], [0, 2], [0, 8], [4, 8], [4, 13]]
        # if fee = 2, [[-1, 0], [-1, 0], [-1, 0], [-1, 5], [1, 5], [1, 8]]
        return table[-1][-1]


s = Solution()
prices = [1,3,7,5,10,3]
fee = 3
print(s.maxProfit(prices, fee))