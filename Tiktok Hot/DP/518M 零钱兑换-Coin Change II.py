from typing import List
"""
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        table[0][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                if j >= coins[i - 1]:
                    table[i][j] = table[i - 1][j] + table[i][j - coins[i - 1]]
                else:
                    table[i][j] = table[i - 1][j]
        # print(table)
        return table[-1][-1]

    def change_top_down(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def recursion(index, value):
            if index == -1:
                return 1 if value == 0 else 0
            if value < 0:
                return 0
            if (index, value) in memo:
                return memo[(index, value)]
            memo[(index, value)] = recursion(index - 1, value) + recursion(index, value - coins[index])
            return memo[(index, value)]

        return recursion(len(coins) - 1, amount)


s = Solution()
amount = 5
coins = [1,2,5]
test = s.change_top_down(amount, coins)
print(test)