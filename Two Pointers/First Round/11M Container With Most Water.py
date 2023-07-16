"""
Runtime: ms609, beat 98%
Difficulty: Median
Solution: two pointers, find the min height of the two pointers and record the max area
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            min_height = min(height[left], height[right])
            area = max(area, (right - left) * min_height)
            if height[left] <= height[right]:
                left += 1
                while height[left] <= min_height and left < right:
                    left += 1
            else:
                right -= 1
                while height[right] <= min_height and left < right:
                    right -= 1
        return area


sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
res = sol.maxArea(height)
print(res)