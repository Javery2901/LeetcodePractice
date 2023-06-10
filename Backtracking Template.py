"""
如何解决重复问题：尽量在for循环中控制index，如前面的index已经遍历过，则不再重新遍历
当for循环可以控制每次递归时的范围时，如循环逐渐缩小，则可以用index来控制
当for循环无法控制每次递归时的范围时，可以考虑用counter计数器
"""

def backtrack(path: list)
    if condition(path):
        return xxxx

    for item in given_array:
        path.append(item)
        backtrack(path)
        path.pop()
    return