class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)


so = Solution()
s = "abbaca"
so.removeDuplicates(s)
test = so.removeDuplicates(s)
print(test)