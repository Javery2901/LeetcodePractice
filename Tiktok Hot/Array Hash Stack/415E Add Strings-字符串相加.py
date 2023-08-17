"""
Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        car = 0
        res = ""
        while num1 or num2 or car:
            if num1:
                car += int(num1.pop())
            if num2:
                car += int(num2.pop())
            res += str((car % 10))
            car //= 10
        return res[::-1]
