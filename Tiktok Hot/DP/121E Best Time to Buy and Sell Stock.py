from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # let's try dp
        # table[i][0] 表示持有时的手头总金额，两种情况：跟昨天一样继续持有的，今天买入后手头减少了之后的
        # table[i][0] 表示未持有时的手头总金额，两种情况：跟昨天一样没有持有的，今天卖出后手头增加了之后的
        table = [[0] * 2 for _ in range(len(prices))]
        table[0][0] = -prices[0]
        for i in range(1, len(prices)):
            table[i][0] = max(table[i - 1][0], -prices[i])
            table[i][1] = max(table[i - 1][1], table[i - 1][0] + prices[i])
        # print(table)
        return table[-1][-1]


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))