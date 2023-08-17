from typing import List
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs_backtracking(l, r, path):
            if l == 0 and r == 0:
                res.append(path)
                return
            if l > 0:
                dfs_backtracking(l - 1, r, path + '(')
            if r > 0 and l < r:
                dfs_backtracking(l, r - 1, path + ')')

        dfs_backtracking(n, n, '')
        return res


s = Solution()
n = 1
test = s.generateParenthesis(n)
print(test)
