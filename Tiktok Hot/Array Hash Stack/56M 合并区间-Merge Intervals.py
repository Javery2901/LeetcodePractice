from typing import List
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # O(nlogn)
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for (i, j) in intervals[1:]:
            if i > end:
                res.append([start, end])
                start, end = i, j
            else:  # i <= end:
                end = max(end, j)
        res.append([start, end])  # important
        return res


s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
test = s.merge(intervals)
print(test)