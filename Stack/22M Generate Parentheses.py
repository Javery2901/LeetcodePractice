"""
Runtime: ms35, beat 8%
Difficulty: Median
Solution: dfs recursion
Time complexity: O(4^n)
Space complexity: O(n)
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(ans, s, left, right):
            if left == 0 and right == 0:
                ans.append(s)
            if left > 0:
                dfs(ans, s + '(', left - 1, right)
            if right > 0 and left < right:
                dfs(ans, s + ')', left, right - 1)

        ans = []
        dfs(ans, '', n, n)
        return ans


sol = Solution()
n = 2
res = sol.generateParenthesis(n)
print(res)
