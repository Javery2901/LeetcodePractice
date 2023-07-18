from cmath import inf
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers, 也是一种greedy想法，从最两边开始，记录面积，从最短边开始移动
        left = 0
        right = len(height) - 1
        max_area = -inf
        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height * (right - left))
            if height[left] <= height[right]:  # left is smaller
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
height = [1,1]
test = s.maxArea(height)
print(test)