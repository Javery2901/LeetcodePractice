class Solution:
    def totalNQueens(self, n: int) -> int:
        # redo again
        res = []
        ls = [[0] * n for _ in range(n)]
        print(ls)
        hori_range = set()
        diag_range = set()
        anti_range = set()

        def deep_copy(ls):
            return [i[:] for i in ls]

        def dfs_backtranking(c, index):
            if index == n:
                res.append(deep_copy(ls))
                return

            for r in range(n):
                if r in hori_range or r - c in diag_range or r + c in anti_range:
                    continue
                ls[r][c] = 1
                hori_range.add(r)
                diag_range.add(r - c)
                anti_range.add(r + c)

                dfs_backtranking(c + 1, index + 1)

                ls[r][c] = 0
                hori_range.remove(r)
                diag_range.remove(r - c)
                anti_range.remove(r + c)

        dfs_backtranking(0, 0)
        return len(res)


s = Solution()
n = 4
test = s.totalNQueens(n)
print(test)