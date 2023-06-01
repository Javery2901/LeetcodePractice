"""
Runtime: ms1328, beat 80%
Difficulty: Median
Solution: stack
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                res[index] = (i-index)
            stack.append([i,v])
        return res


sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
res = sol.dailyTemperatures(temperatures)
print(res)