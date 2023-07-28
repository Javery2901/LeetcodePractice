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

    def minCostConnectPoints_Kruskal(self, points: List[List[int]]) -> int:
        # kruskal using edge list

        ls = [i for i in range(len(points))]
        # 需要将每个点与ls对应上
        dic = {}
        for i, point in enumerate(points):
            dic[tuple(point)] = i

        def find(x, ls):
            if x == ls[x]:
                return x
            cur = x
            while cur != ls[cur]:
                cur = ls[cur]
            return cur

        def union(x, y, ls):
            x_parent = find(x, ls)
            y_parent = find(y, ls)
            if x_parent != y_parent:
                ls[x_parent] = y_parent
            return

        def distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        cost = 0
        edge_count = 0
        edge_list = []

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edge_list.append((distance(points[i], points[j]), points[i], points[j]))

        edge_list.sort()  # this is huge
        for edge_info in edge_list:
            if edge_count == len(points) - 1:  # 当有edge_count的边被连起来是则说明全部连起来了
                break
            weight, point1, point2 = edge_info
            p1, p2 = dic[tuple(point1)], dic[tuple(point2)]
            if find(p1, ls) != find(p2, ls):
                cost += weight
                union(p1, p2, ls)
                edge_count += 1
        return cost


s = Solution()
points = [[3,12],[-2,5],[-4,1]]
test = s.minCostConnectPoints(points)
print(test)