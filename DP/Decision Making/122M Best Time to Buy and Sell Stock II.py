from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [0] * len(prices)
        for i in range(1, len(prices)):
            table[i] = max(0, prices[i] - prices[i - 1]) + table[i - 1]
        return table[-1]


