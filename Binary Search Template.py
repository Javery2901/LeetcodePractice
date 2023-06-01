"""
Minimise k such that condition(k) is True

When to use binary search:
If we can discover some kind of monotonicity, for example,
if condition(k) is True, then condition(k + 1) is True
we can consider binary search
"""


def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)
    # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# After existing the while loop, left is the minimal k satisfying the condition function
