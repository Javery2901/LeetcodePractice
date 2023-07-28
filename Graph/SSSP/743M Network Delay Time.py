import collections
import heapq

from cmath import inf
from typing import List


class Solution:
    def networkDelayTime_modified_dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        # modified dijkstra
        al = collections.defaultdict(list)
        for u, v, w in times:
            al[u].append((w, v))
        # print(al)  # {2: [(1, 1), (1, 3)], 3: [(1, 4)]}

        distance = [inf if i != k else 0 for i in range(n + 1)]  # [1, n]
        hp = []
        heapq.heappush(hp, (0, k))  # (weight, node)
        while hp:
            dist, pop_node = heapq.heappop(hp)
            if dist > distance[pop_node]:  # distance中存储的是至目前为止的权重最小值
                # 若dist大于distance，则说明这条路不是最佳路线，无意义
                continue
            for d, neighbor in al[pop_node]:
                if distance[pop_node] + d >= distance[neighbor]:
                    # 如果从前一个节点到他的neighbor节点，权重值超过了neighbor目前的权重值，
                    # 则说明这条路线不是最佳路线，不需要将他考虑下去
                    continue
                distance[neighbor] = distance[pop_node] + d
                heapq.heappush(hp, (distance[neighbor], neighbor))
        # print(distance)
        if inf in distance[1:]:
            return -1
        return max(distance[1:])

    def networkDelayTime_dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)

        for x, y, w in times:
            adj_list[x].append((w, y))

        visited = set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)

            if len(visited) == n:
                return travel_time

            for time, adjacent_node in adj_list[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time + time, adjacent_node))

        return -1


s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
test = s.networkDelayTime_modified_dijkstra(times, n, k)
print(test)
