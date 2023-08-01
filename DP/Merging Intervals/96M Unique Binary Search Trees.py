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
        # 理解：每个树可以看作是左右两个子树数量的乘积，即若n = 3
        # 左子树有0个数时，右子树有2个数：table[0] * table[2]; 左子树有1个数时，右子树有1个数：table[1] * table[1];
        # 左子树有2个数时，右子树有1个数：table[2] * table[0];
        # 相加即为答案
        table = [0] * (n + 1)
        table[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                table[i] += table[j] * table[i - j - 1]
        return table[n]


s = Solution()
n = 2
test = s.numTrees_bottom_up(n)
print(test)