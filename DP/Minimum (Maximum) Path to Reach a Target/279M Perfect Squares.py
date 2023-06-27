import math
"""
this is the same as coin change
"""

class Solution:
    def numSquares_top_down(self, n: int) -> int:
        heuristic = []
        for i in range(1, 101):
            heuristic.append(i ** 2)
        memo = {}

        def dp(n, memo):
            if n < 0:
                return math.inf
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(1 + dp(n - x, memo) for x in heuristic if x <= n)
            return memo[n]

        memo[n] = dp(n, memo)
        # print(memo)
        return memo[n]

    def numSquares_bottom_up(self, n: int) -> int:
        heuristic = []
        for i in range(1, 101):
            heuristic.append(i ** 2)

        table = [0] + [10000] * n
        for i in range(1, n + 1):
            for perfect_square in heuristic:
                if perfect_square > i:
                    break
                if perfect_square <= i:
                    table[i] = min(table[i], table[i - perfect_square] + 1)
        return table[n]


s = Solution()
n = 6603
test = s.numSquares_bottom_up(n)
print(test)