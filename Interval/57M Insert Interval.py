from math import inf
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            return [newInterval]

        def interval(i, insert_ls):
            if i == len(intervals):
                res.append(insert_ls)
                return
            x, y = intervals[i][0], intervals[i][1]
            if x > insert_ls[1]:
                res.append(insert_ls)
                res.extend(intervals[i:])
                return
            elif y < insert_ls[0]:
                res.append(intervals[i])
                interval(i + 1, newInterval)
            else:
                start = min(x, insert_ls[0])
                end = max(y, insert_ls[1])
                interval(i + 1, [start, end])

        interval(0, newInterval)

        return res


s = Solution()
intervals = [[1,5]]
newInterval = [6,8]
test = s.insert(intervals, newInterval)
print(test)