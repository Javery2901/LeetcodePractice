import math
"""
this is the same as coin change
"""

class Solution:
    def numSquares_top_down(self, n: int) -> int:
        memo = {}

        def recursion(number):
            if number == 0:
                return 0
            if number < 0:
                return math.inf
            if number in memo:
                return memo[number]
            res = math.inf
            for i in range(1, int(math.sqrt(number) + 1)):
                res = min(res, 1 + recursion(number - i ** 2))
            memo[number] = res
            return memo[number]

        return recursion(n)

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