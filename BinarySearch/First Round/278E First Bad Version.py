# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
"""
Runtime: ms38, beat 42%
Difficulty: Median
Solution: binary search
Time complexity: O(logn)
Space complexity: O(1)
"""


class Solution:

    def isBadVersion(self, mid):
        pass

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
n = 8
res = sol.firstBadVersion(n)
print(res)
