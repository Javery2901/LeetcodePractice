"""
Runtime: ms47, beat 55%
Difficulty: Easy
Solution: binary search
Time complexity: O(logn)
Space complexity: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1  # deal with special cases like x = 0 or x = 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1  # left is the minimum k value satisfying the mid * mid > x
        # that's why we should return left - 1


sol = Solution()
x = 8
res = sol.mySqrt(x)
print(res)
