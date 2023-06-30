import collections


class Solution:
    def findPaths_top_down(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
            memo = {}  # {((i, j), current_move) = # of paths}

            def valid(i, j):
                if 0 <= i < m and 0 <= j < n:
                    return True
                return False

            def dfs(i, j, current_move):
                if not valid(i, j):
                    if current_move <= maxMove:
                        return 1
                else:
                    if current_move >= maxMove:
                        return 0
                if (i, j, current_move) in memo:
                    return memo[(i, j, current_move)]
                memo[(i, j, current_move)] = dfs(i - 1, j, current_move + 1) + dfs(i + 1, j, current_move + 1) + \
                                             dfs(i, j - 1, current_move + 1) + dfs(i, j + 1, current_move + 1)
                return memo[(i, j, current_move)]

            dfs(startRow, startColumn, 0)
            # print(memo)
            return memo[(startRow, startColumn, 0)] % (10 ** 9 + 7)

    def findPaths_bottom_up(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        table = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        table[startRow][startColumn][0] = 1
        count = 0

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if table[i][j][k] > 0:
                        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                            if valid(x, y):
                                table[x][y][k + 1] += table[i][j][k]
                            else:
                                count += table[i][j][k]
        return count % (10 ** 9 + 7)

    def findPaths_bfs(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # bfs  Memory limited exceed
        queue = collections.deque([(startRow, startColumn)])
        res = 0

        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        while queue:
            if maxMove < 0:
                break
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if not valid(row, col):
                    res += 1
                    if res == 10 ** 9 + 7:
                        res = 0
                    continue
                for x, y in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    queue.append((x, y))
            maxMove -= 1
        return res % (10 ** 9 + 7)


s = Solution()
m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
test = s.findPaths_bfs(m, n, maxMove, startRow, startColumn)
print(test)
