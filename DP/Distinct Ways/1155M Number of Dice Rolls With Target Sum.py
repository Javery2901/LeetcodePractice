class Solution:
    def numRollsToTarget_bottom_up(self, n: int, k: int, target: int) -> int:
        # table[n][target] = table[n-1][1] + table[n-1][2] + ... + table[n-1][target-1]
        # time: O(n * k * target)
        # space: O(n * target)
        if target < n or target > n * k:
            return 0
        """
           1  2  3  4  5  6  7  8  (target) let's say k == 4
        1  1  1  1  1  0  0  0  0  
        2  0  1  2  3  4  3  2  1  
        3  0  0  1  3  6  10 12 12 
        (n)
        理解：假设target = 8， n = 3，k = 4，那么当3副牌都是用加和为8的情况
        其实等于，2副牌加和为7的情况 + 2副牌加和为6的情况 + 2副牌加和为5的情况 + 2副牌加和为4的情况
        情况的数量取决于k值，因为对第三副牌来说，它就只有k种取值
        """
        table = [[0] * (1 + target) for _ in range(n + 1)]
        for i in range(1, 1 + n):
            for j in range(1, 1 + target):
                for step in range(1, k + 1):
                    if i == 1 and j <= k:
                        table[i][j] = 1
                        break
                    else:
                        if j - step > 0:
                            table[i][j] += table[i - 1][j - step]
        # print(table)

        return table[-1][-1] % (10 ** 9 + 7)


s = Solution()
n = 30
k = 30
target = 500
test = s.numRollsToTarget_bottom_up(n, k, target)
print(test)