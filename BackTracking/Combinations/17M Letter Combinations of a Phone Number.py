from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        res = []
        if not digits:
            return res

        def backtracking(index, string):
            if index == len(digits):
                res.append(string)
                return

            for i in map[digits[index]]:
                backtracking(index + 1, string + i)

        backtracking(0, '')
        return res


s = Solution()
digits = "2"
print(s.letterCombinations(digits))
