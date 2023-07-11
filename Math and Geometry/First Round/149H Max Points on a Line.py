import collections
from math import inf
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:  # the memory required is huge
        if len(points) == 1:
            return 1

        def slope_and_intercept(point1, point2):
            k = inf if point2[0] - point1[0] == 0 else (point2[1] - point1[1]) / (point2[0] - point1[0])
            b = point1[0] if k == inf else point1[1] - point1[0] * k
            return k, b

        slope_intercept_dict = collections.defaultdict(set)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                slope, intercept = slope_and_intercept(points[i], points[j])
                slope_intercept_dict[(slope, intercept)].add((points[i][0], points[i][1]))
                slope_intercept_dict[(slope, intercept)].add((points[j][0], points[j][1]))
        # print(slope_intercept_dict)

        max_v = 1
        for k, v in slope_intercept_dict.items():
            max_v = max(len(v), max_v)
        return max_v

    def maxPoints_optimal(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            delta_x = x1 - x2
            if delta_x == 0:
                return float('inf')
            return (y1 - y2) / delta_x

        ans = 1
        for i, p1 in enumerate(points):
            slopes = collections.defaultdict(int)
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1


s = Solution()
points = [[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]]
test = s.maxPoints(points)
print(test)
