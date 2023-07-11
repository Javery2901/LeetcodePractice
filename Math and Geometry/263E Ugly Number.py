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