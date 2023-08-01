class Solution:
    def integerBreak(self, n: int) -> int:
        # 解题思路：table存储的是每个n的答案值，即拆分后相乘的最大值
        # 对数字i来说，拆出的整数是j和i - j，且i - j 不再拆分，则结果为 j * (i - j)
        # 若继续拆分，则结果为j * table[i - j]
        # 理解：上面的j 和i - j可以看作是，从前遍历时，当第一个数时j时，另一个数直接计算。
        # 但i - j有可能是可以继续拆分的，因此是table[i - j]
        table = [0] * (n + 1)
        table[2] = 1
        # [0,0,1,2,4,6,9,12,18,27,36]
        for i in range(3, n + 1):
            for j in range(1, i):
                table[i] = max(table[i], j * table[i - j], j * (i - j))
        # print(table)  # [0, 0, 1, 2, 4, 6, 9, 12, 18, 27, 36]
        return table[-1]

    def integerBreak_2(self, n: int) -> int:
        # 方法2，理解：table[i]代表每次至少是两个数相乘
        # 因此 table[j] * table[i - j 代表至少四个数相乘的最大结果
        # 因此需要初始化table至4
        table = [1] * (n + 1)
        if n == 2:
            return 1
        if n == 3:
            return 2
        table[2], table[3] = 2, 3
        # [1,2,3,4,6,9,12,18,27,36]
        for i in range(4, n + 1):
            table[i] = max(table[j] * table[i - j] for j in range(1, i))
        return table[-1]

s = Solution()
n = 10
print(s.integerBreak(n))