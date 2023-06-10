from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        heuristic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
                     }
        if not digits:
            return []
        res = []
        n = len(digits)
        substr = ''

        def dfs_backtracking(index, substr):
            if index == n:
                res.append(substr)
                return
            for letter in heuristic[digits[index]]:
                dfs_backtracking(index + 1, substr + letter)

        dfs_backtracking(0, substr)
        return res


s = Solution()
digits = ''
test = s.letterCombinations(digits)
print(test)
