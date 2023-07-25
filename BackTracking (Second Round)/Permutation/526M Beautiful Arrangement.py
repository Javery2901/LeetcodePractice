class Solution:
    def __init__(self):
        self.res = 0

    def countArrangement(self, n: int) -> int:
        counter = [False] * (1 + n)

        def backtracking(index):
            if index == n:
                self.res += 1
                return
            for number in range(1, n + 1):
                if not counter[number] and (number % (index + 1) == 0 or (index + 1) % number == 0):
                    counter[number] = True
                    backtracking(index + 1)
                    counter[number] = False

        backtracking(0)
        return self.res


s = Solution()
n = 3
test = s.countArrangement(n)
print(test)