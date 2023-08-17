import collections


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [['d', 3],[],[]]
        for i in s:
            if stack and stack[-1][0] == i: # 如果最后一位等于i
                stack[-1][1] += 1
                if stack[-1][1] == k:  # 判断连续出现的次数
                    stack.pop()
            else:
                stack.append([i, 1])
        # print(stack)
        res = ''
        for ch, freq in stack:
            res += ch * freq
        return res


so = Solution()
s = "pbbcggttciiippooaais"
k = 2
test = so.removeDuplicates(s, k)
print(test)
