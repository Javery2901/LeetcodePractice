class Solution:
    def uniquePaths_bottom_up(self, m: int, n: int) -> int:
        # 构建表格，表格的是结果与其上一位和左一位相关，因为只能从这两个地方到达这里
        table = [[0] * (1 + n) for _ in range(m + 1)]
        table[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m][n]

    def uniquePaths_top_down(self, m: int, n: int) -> int:
        memo = {}

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True

        def sub_unique_paths(i, j, memo):
            if not valid(i, j):
                return 0
            if i == 0 and j == 0:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = sub_unique_paths(i - 1, j, memo) + sub_unique_paths(i, j - 1, memo)
            return memo[(i, j)]

        return sub_unique_paths(m - 1, n - 1, memo)


s = Solution()
m = 3
n = 7
test = s.uniquePaths_top_down(m, n)
print(test)