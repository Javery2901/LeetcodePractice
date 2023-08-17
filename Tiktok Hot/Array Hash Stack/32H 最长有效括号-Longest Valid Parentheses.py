class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]  # 初始化为-1，作为dummy head，类似于指向每一个正式开始的前一个
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # 放入序号
            else:
                stack.pop()
                # 如果pop后，即整个stack空了，说明pop掉的有问题，不可能是valid的
                # 如果还有，说明pop掉的是一个valid的（
                if not stack:
                    stack.append(i) # 加入当前这个肯定有问题的）
                else:
                    # 非空，更新一次res
                    res = max(res, i - stack[-1])
        return res

    def longestValidParentheses2(self, s: str) -> int:
        max_length = 0

        l, r = 0, 0
        # traverse the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif r > l:  # invalid case as ')' is more
                l = r = 0
        # ((),这种问题出现，需要从后往前再来一次，确保（不会多
        l, r = 0, 0
        # traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:  # valid balanced parantheses substring
                max_length = max(max_length, l * 2)
            elif l > r:  # invalid case as '(' is more
                l = r = 0
        return max_length

so = Solution()
s = "()(()"
test = so.longestValidParentheses2(s)
print(test)