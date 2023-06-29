class Solution:
    def fib_top_down(self, n: int) -> int:  # memoization
        memo = {}

        def fib_helper(n, memo):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = fib_helper(n-1, memo) + fib_helper(n-2, memo)
            return memo[n]
        return fib_helper(n, memo)

    def fib_bottom_up(self, n: int) -> int:  # dynamic programming
        table = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                table[i] = 0
            elif i == 1:
                table[i] = 1
            else:
                table[i] = table[i - 1] + table[i - 2]
        return table[n]

s = Solution()
n = 3
test = s.fib_bottom_up(n)
print(test)