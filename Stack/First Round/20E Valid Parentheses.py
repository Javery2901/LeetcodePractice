"""
Runtime: ms40, beat 35%
Difficulty: Easy
Solution: use a dict to save the information
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        heuristic = {'(':0, ')':1, '[':2, ']':3, '{':4, '}':5}
        stack = []
        for i in s:
            if heuristic[i] % 2 == 0:
                stack.append(i)
            else:
                if heuristic[stack[-1]] == heuristic[i] - 1:
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        else:
            return False


sol = Solution()
s = "(]"
res = sol.isValid(s)
print(res)