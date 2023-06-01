"""
Runtime: ms88, beat 26%
Difficulty: Median
Solution: use stack
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {'+', '-', '*', '/'}
        stack = []
        for i in tokens:
            if i in oper:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    ret = b + a
                elif i == '-':
                    ret = b - a
                elif i == '*':
                    ret = b * a
                else:
                    ret = b // a
                    if ret < 0 and b % a != 0:
                        ret += 1
                stack.append(ret)
            else:
                stack.append(int(i))
        return stack.pop()


sol = Solution()
tokens = ["4","-2","/","2","-3","-","-"]
res = sol.evalRPN(tokens)
print(res)