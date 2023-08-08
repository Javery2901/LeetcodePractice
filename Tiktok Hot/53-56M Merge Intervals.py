from typing import List


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
        res.append([start, end])
        return res


s = Solution()
intervals = [[1,4],[2,3]]
test = s.merge(intervals)
print(test)