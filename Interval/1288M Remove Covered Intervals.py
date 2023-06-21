from typing import List
"""
sort, then the interval[0] will always be covered by the former one
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # print(intervals)  # [[1, 4], [2, 8], [2, 9], [3, 6], [3, 7]]
        left, right = intervals[0][0], intervals[0][1]
        res = 0
        for inter in intervals[1:]:
            if inter[0] == left:
                res += 1
                right = max(right, inter[1])
            else:  # left right始终保持最宽范围
                if inter[1] <= right:
                    res += 1
                else:
                    left = inter[0]
                    right = inter[1]

        return len(intervals) - res


s = Solution()
intervals = [[1,4],[2,3]]
test = s.removeCoveredIntervals(intervals)
print(test)