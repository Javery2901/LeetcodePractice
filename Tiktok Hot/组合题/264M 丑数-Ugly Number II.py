import heapq
"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
"""

class Solution:
    def nthUglyNumber_heapq(self, n: int) -> int:
        if n == 1:
            return 1
        res = []
        heapq.heappush(res, 1)
        existed = {1}
        for _ in range(n - 1):
            num = heapq.heappop(res)
            for factor in (2, 3, 5):
                if num * factor not in existed:
                    heapq.heappush(res, num * factor)
                    existed.add(num * factor)
        return res[0]

    def nthUglyNumber_bottom_up(self, n: int) -> int:
        table = [0] * n
        table[0] = 1
        i, j, k = 0, 0, 0

        for m in range(1, n):
            table[m] = min(table[i] * 2, table[j] * 3, table[k] * 5)
            if table[m] == table[i] * 2:
                i += 1
            if table[m] == table[j] * 3:
                j += 1
            if table[m] == table[k] * 5:
                k += 1
        return table[n - 1]


s = Solution()
n = 11
test = s.nthUglyNumber_bottom_up(n)
print(test)