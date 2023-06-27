from math import inf
from typing import List


class Solution:
    def coinChange_top_down(self, coins: List[int], amount: int) -> int:
        memo = {}  # key: amount, value: fewest number of coins to make up that amount

        def dfs(rest, memo):
            if rest < 0:
                return inf
            if rest == 0:
                return 0
            if rest in memo:
                return memo[rest]
            memo[rest] = 1 + min(dfs(rest - x, memo) for x in coins)
            return memo[rest]

        memo[amount] = dfs(amount, memo)
        # print(memo)
        if memo[amount] == inf:
            return -1
        return memo[amount]

    def coinChange_bottom_up(self, coins: List[int], amount: int) -> int:
        table = [inf] * (amount + 1)
        table[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if i - coin >= 0:
                    table[i] = min(table[i], table[i-coin] + 1)
        return -1 if table[-1] == inf else table[-1]


s = Solution()
coins = [1, 2, 5]
amount = 11
test = s.coinChange_top_down(coins, amount)
print(test)
