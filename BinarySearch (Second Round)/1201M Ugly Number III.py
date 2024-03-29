import heapq
import math
"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
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
