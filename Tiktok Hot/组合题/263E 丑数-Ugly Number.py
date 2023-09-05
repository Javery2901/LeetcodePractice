"""
丑数 就是只包含质因数 2、3 和 5 的正整数。
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

输入：n = 6
输出：true
解释：6 = 2 × 3
"""

class Solution:
    def isUgly(self, n: int) -> bool:

        def recursion(num):
            if num == 0:
                return False
            if num == 1:
                return True
            if num % 2 == 0:
                return recursion(num // 2)
            if num % 3 == 0:
                return recursion(num // 3)
            if num % 5 == 0:
                return recursion(num // 5)
            return False

        return recursion(n)


s = Solution()
n = 14
test = s.isUgly(n)
print(test)