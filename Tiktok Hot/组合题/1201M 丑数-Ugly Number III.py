import heapq
import math
"""
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数 。

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
"""


class Solution:
    def nthUglyNumber_heapq(self, n: int, a: int, b: int, c: int) -> int:
        # try easy first  TLE
        res = 0
        i, j, k = 1, 1, 1

        for _ in range(n):
            res = min(a * i, b * j, c * k)
            if res == a * i:
                i += 1
            if res == b * j:
                j += 1
            if res == c * k:
                k += 1
        return res

    def nthUglyNumber_binary_search(self, n: int, a: int, b: int, c: int) -> int:

        def enough(num) -> bool:
            total = num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc
            return total >= n

        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)
        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
n = 1000000000
a = 2
b = 217983653
c = 336916467
test = s.nthUglyNumber_binary_search(n, a, b, c)
print(test)
