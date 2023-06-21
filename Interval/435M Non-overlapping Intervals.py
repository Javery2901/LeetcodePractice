from typing import List
"""
Concept: three cases after sorting:
1: [1,3], [3,4], we update a pointer from 3 to 4
2: [1,5], [2,3], we update a pointer from 5 to 3, res += 1
3. [1,3], [2,4], we dont update the pointer, res += 1
rule: pointer is the one ends first
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pointer = intervals[0][1]
        res = 0
        for inter in intervals[1:]:
            # sorted, important
            i, j = inter[0], inter[1]
            if i >= pointer:  # case 1
                pointer = j
            else:
                if j <= pointer:  # case 2
                    pointer = j
                    res += 1
                else:
                    res += 1  # case 3
        return res


s = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
test = s.eraseOverlapIntervals(intervals)
print(test)