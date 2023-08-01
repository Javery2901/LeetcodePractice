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

    def coinChange_bottom_up2(self, coins: List[int], amount: int) -> int:
        table = [[inf] * (amount + 1) for _ in range(len(coins) + 1)]
        # for i in range(amount + 1):
        #     table[0][i] = 0
        table[0][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                if j >= coins[i - 1]:
                    table[i][j] = min(table[i - 1][j], table[i][j - coins[i - 1]] + 1)
                else:
                    table[i][j] = table[i - 1][j]
        # print(table)
        return table[-1][-1] if table[-1][-1] != inf else -1

s = Solution()
coins = [1, 2, 5]
amount = 11
test = s.coinChange_bottom_up2(coins, amount)
print(test)
