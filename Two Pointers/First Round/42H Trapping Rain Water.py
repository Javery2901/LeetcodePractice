"""
Runtime: ms139, beat 44%
Difficulty: Median
Solution:
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        old_min_height = 0
        while l < r:
            min_height = min(height[l], height[r])
            area = area - old_min_height + (r - l - 1) * (min_height - old_min_height)
            if height[l] == min_height:
                l += 1
                while height[l] <= min_height and l < r:
                    area -= height[l]
                    l += 1
            else:
                r -= 1
                while height[r] <= min_height and l < r:
                    area -= height[r]
                    r -= 1
            old_min_height = min_height
        return area


sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
res = sol.trap(height)
print(res)
