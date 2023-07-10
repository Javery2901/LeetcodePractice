"""
Minimise k such that condition(k) is True

When to use binary search:
If we can discover some kind of monotonicity, for example,
if condition(k) is True, then condition(k + 1) is True
we can consider binary search
"""

"""
第一种写法，左闭右闭。[left, right]
while left <= right, 因为left == right 有意义
if nums[mid] > target, right 需赋值为 mid - 1, 
因为当前nums[mid]一定不是target，那么接下来要查找的区间的最右端应该是mid-1 (因为right值可以被取到)

第二种写法，左闭右开。[left, right)
while left < right， 因为left == right无意义
if nums[mid] > target, right 需赋值为 mid, 
因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，
所以right更新为middle，即：下一个查询区间不会去比较nums[middle]
"""


def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)
    # could be [0, n], [1, n] etc. Depends on problem
    # keys: include all possible elements
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
    # After existing the while loop, left is the minimal k satisfying the condition function
