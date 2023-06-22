import heapq
from typing import List
"""
要点，排完序后需根据需要将intervals进行特殊处理，heapq.heappush(pq, (end - start + 1, end))
加入的第一个元素为要求的值，end - start + 1。第二个元素是上限边界
"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        # queries needs to be sorted(), but also needs to record the index
        queries_sort = []
        for i, n in enumerate(queries):
            queries_sort.append((n, i))
        queries_sort.sort()
        # print(queries_sort)  # [(2, 0), (5, 2), (19, 1), (22, 3)]
        intervals.sort(reverse=True)
        print(intervals)  # [[20, 25], [2, 5], [2, 3], [1, 8]]

        pq = []
        for query, i in queries_sort:
            while len(intervals) and query >= intervals[-1][0]:
                start, end = intervals.pop()
                heapq.heappush(pq, (end - start + 1, end))  # end的作用是截断
                # [(2, 3), (6, 25), (4, 5), (8, 8)]  meaning：截至到3的数，interval为2。截至到25，interval为6
            while len(pq) and query > pq[0][1]:
                heapq.heappop(pq)
            if len(pq) != 0:
                res[i] = pq[0][0]
        return res


s = Solution()
intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]
test = s.minInterval(intervals, queries)
print(test)
