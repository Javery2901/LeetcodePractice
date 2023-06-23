class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def _add(n):
            res = 0
            string = str(n)
            for i in string:
                res += int(i) * int(i)
            if res == 1:
                return True
            if res in visited:
                return False
            visited.add(res)
            return _add(res)

        return _add(n)


s = Solution()
n = pow(2,31) - 1
test = s.isHappy(n)
print(test)