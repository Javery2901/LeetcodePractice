"""
给定一个经过编码的字符串，返回它解码后的字符串。
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


so = Solution()
s = "3[a]2[bc]"
test = so.decodeString(s)
print(test)