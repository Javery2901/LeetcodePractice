from typing import List


class Solution:
    def maxProfit_sliding_window(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                res += prices[right] - prices[left]
            left = right
        return res

    def maxProfit_greedy(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res


s = Solution()
prices = [7,1,5,3,6,4]
test = s.maxProfit_greedy(prices)
print(test)