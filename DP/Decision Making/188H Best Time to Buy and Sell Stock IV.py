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


s = Solution()
k = 2
prices = [2,4,1]
test = s.maxProfit(k, prices)
print(test)