from typing import List
import heapq
"""
最小生成树
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # PRIM algorithm, start from points[0]
        visited = {(points[0][0], points[0][1])}

        def add_all_distance(i, j, ls):
            for point in points:
                x, y = point[0], point[1]
                if (x, y) in visited:
                    continue
                ls.append(((x, y), (abs(i-x) + abs(j-y))))
            return ls

        pq = []
        neighbor = add_all_distance(points[0][0], points[0][1], [])
        # print(neighbor)  # [((2, 2), 4), ((3, 10), 13), ((5, 2), 7), ((7, 0), 7)]
        for neighbor_node, dist in neighbor:
            heapq.heappush(pq, (dist, neighbor_node))
        mst_cost = 0
        num_taken = 0

        while pq and num_taken < len(points) - 1:
            weight, node = heapq.heappop(pq)
            if node in visited:  # 对一个很远的点来说，由于他一直没加入在visited里，其余点与他的距离就会多次出现在pq中
                continue
            visited.add(node)  # node: (2, 2)
            mst_cost += weight
            num_taken += 1
            neighbor = add_all_distance(node[0], node[1], [])
            for neighbor_node, dist in neighbor:
                heapq.heappush(pq, (dist, neighbor_node))
        return mst_cost


s = Solution()
points = [[3,12],[-2,5],[-4,1]]
test = s.minCostConnectPoints(points)
print(test)