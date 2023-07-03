class Solution:
    def knightProbability_top_down(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}

        def valid(r, c):
            if 0 <= r < n and 0 <= c < n:
                return True
            return False

        def recursion(r, c, k, memo):
            if k < 0:
                return 1
            if not valid(r, c):
                return 0
            if (r, c, k) in memo:
                return memo[(r, c, k)]
            memo[(r, c, k)] = 0
            for x, y in ((r - 1, c - 2), (r - 1, c + 2), (r - 2, c - 1), (r - 2, c + 1),
                         (r + 1, c - 2), (r + 1, c + 2), (r + 2, c - 1), (r + 2, c + 1),):
                memo[(r, c, k)] += 1 / 8 * recursion(x, y, k - 1, memo)

            return memo[(r, c, k)]

        recursion(row, column, k, memo)
        print(memo)
        return round(memo[(row, column, k)], 5)

    def knightProbability_bottom_up(self, n: int, k: int, row: int, column: int) -> float:
        table = [[1] * n for _ in range(n)]

        # def valid(r, c):  # this is slow
        #     if 0 <= r < n and 0 <= c < n:
        #         return True
        #     return False

        for i in range(k):
            memo = [i[:] for i in table]
            for r in range(n):
                for c in range(n):
                    table[r][c] = 0
                    for x, y in ((r - 1, c - 2), (r - 1, c + 2), (r - 2, c - 1), (r - 2, c + 1),
                                 (r + 1, c - 2), (r + 1, c + 2), (r + 2, c - 1), (r + 2, c + 1),):
                        if 0 <= x < n and 0 <= y < n:
                            table[r][c] += memo[x][y] * (1 / 8)
        print(table)
        return round(table[row][column], 5)


s = Solution()
n = 10
k = 13
row = 5
column = 3
test = s.knightProbability_bottom_up(n, k, row, column)
print(test)
