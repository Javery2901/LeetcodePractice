import collections


class Solution:
    def numTrees_top_down(self, n: int) -> int:
        memo = collections.defaultdict(int)

        def recursion(i):
            if i == 0 or i == 1:
                return 1
            if i in memo:
                return memo[i]
            for j in range(i):
                memo[i] += recursion(j) * recursion(i - j - 1)
            return memo[i]

        return recursion(n)

    def numTrees_bottom_up(self, n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                table[i] += table[j] * table[i - j - 1]
        return table[n]


s = Solution()
n = 3
test = s.numTrees_bottom_up(n)
print(test)