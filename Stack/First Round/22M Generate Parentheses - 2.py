"""
Runtime: ms53, beat 21%
Difficulty: Median
Solution: dfs iteration
Time complexity: O()
Space complexity: O()
"""
from typing import List
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        ans = []
        queue = deque([("", n, n)])  # 初始状态：空字符串，剩余左括号数和右括号数都为n

        while queue:
            s, left, right = queue.popleft()

            if left == 0 and right == 0:
                ans.append(s)

            if left > 0:
                queue.append((s + '(', left - 1, right))

            if right > 0 and left < right:
                queue.append((s + ')', left, right - 1))

        return ans


sol = Solution()
n = 2
res = sol.generateParenthesis(n)
print(res)
