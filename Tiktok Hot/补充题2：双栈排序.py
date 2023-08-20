"""
给定一个乱序的栈，设计算法将其升序排列。允许使用一个栈来辅助操作
[4,2,1,3] -> [1,2,3,4]
"""

def stacksort(stack):
    helper_stack = []
    while stack:
        pop_node = stack.pop()
        while helper_stack and helper_stack[-1] > pop_node:
            stack.append(helper_stack.pop())
        helper_stack.append(pop_node)
    return helper_stack


stack = [4,2,1,3]
print(stacksort(stack))
