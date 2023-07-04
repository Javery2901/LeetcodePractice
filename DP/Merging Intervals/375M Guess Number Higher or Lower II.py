from functools import cache


class Solution:
    def getMoneyAmount_top_down(self, n: int) -> int:
        memo = {}

        # time: O(n ** 3)
        # space: O(n ** 2)

        def recursion(low: int, high: int):
            if high == low:
                return 0
            if high - low == 1:
                return low
            if (low, high) in memo:
                return memo[(low, high)]
            memo[(low, high)] = min(i + max(recursion(low, i - 1), recursion(i + 1, high))
                                    for i in range(low + 1, high))
            # i is the current guess,
            # if the truth is lower than i, pay recursion(low, i - 1)
            # if the truth is higher than i, pay recursion(i + 1, high)
            return memo[(low, high)]

        # recursion(1, n)
        # print(memo)
        return recursion(1, n)

    def getMoneyAmount_cache(self, n: int) -> int:
        # time: O(n ** 3)
        # space: O(n ** 2)

        @cache
        def recursion(low: int, high: int):
            if high == low:
                return 0
            if high - low == 1:
                return low
            # i is the current guess,
            # if the truth is lower than i, pay recursion(low, i - 1)
            # if the truth is higher than i, pay recursion(i + 1, high)
            return min(i + max(recursion(low, i - 1), recursion(i + 1, high)) for i in range(low + 1, high))

        return recursion(1, n)


s = Solution()
n = 10
test = s.getMoneyAmount_cache(n)
print(test)
