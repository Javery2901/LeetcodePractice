from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtracking(index, substring):
            if len(substring) == len(s):
                res.append(substring)
                return
            if s[index].isnumeric():
                backtracking(index + 1, substring + s[index])
            else:
                backtracking(index + 1, substring + s[index].lower())
                backtracking(index + 1, substring + s[index].upper())

        backtracking(0, '')
        return res


so = Solution()
s = "3z4"
test = so.letterCasePermutation(s)
print(test)