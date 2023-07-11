from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x * x + y * y

        res = []
        heap = []
        for point in points:
            x, y, dis = point[0], point[1],  distance(point[0], point[1])
            if len(heap) == k:
                heapq.heappushpop(heap, (-dis, [x, y]))
            else:
                heapq.heappush(heap, (-dis, [x, y]))
        while heap:
            _, point = heapq.heappop(heap)
            res.append(point)
        return res


s = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
test = s.kClosest(points, k)
print(test)
