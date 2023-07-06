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
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 8]
test = s.maxProfit_greedy(prices)
print(test)
