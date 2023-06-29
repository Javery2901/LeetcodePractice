class Solution:
    def climbStairs_bottom_up(self, n: int) -> int:
        # this is actually also a fibonacci problem
        table = [1] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                table[i] = 1
            else:
                table[i] = table[i - 1] + table[i - 2]
        return table[n]

    def climbStairs_top_down(self, n: int) -> int:
        memo = {}

        def dfs(n, memo):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
            return memo[n]
        return dfs(n, memo)


s = Solution()
n = 1
test = s.climbStairs_top_down(n)
print(test)
