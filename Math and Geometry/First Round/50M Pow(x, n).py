class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1

        # 可使用二分法： 2^10 == 2^(2*5) == 4^5 == 4*4^4 == 4*16^2 == 4*256^1 == 4*256

        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n = n // 2
        return res


s = Solution()
x = 1
n = 2147483647
test = s.myPow(x, n)
print(test)
