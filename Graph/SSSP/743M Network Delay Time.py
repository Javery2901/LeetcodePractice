import collections
import heapq
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # SSSP
        AL = collections.defaultdict(list)
        for t in times:
            AL[t[0]].append((t[1], t[2]))
        if n == 1:
            return 0
        if not AL[k]:
            return -1
        dist = [0 if i == k else inf for i in range(n + 1)]
        pq = []
        visited = set()
        heapq.heappush(pq, (0, k))
        while pq:
            d, u = heapq.heappop(pq)  # 0, 2
            if u not in visited:
                visited.add(u)
            if d > dist[u]:  # this step is very important
                continue
            for v, w in AL[u]:
                if w + dist[u] >= dist[v]:  # this is >=, very important
                    continue
                dist[v] = w + dist[u]
                heapq.heappush(pq, (dist[v], v))
        if len(visited) < n:
            return -1
        return max(dist[1:])


s = Solution()
times = [[1,2,1]]
n = 2
k = 2
test = s.networkDelayTime(times, n, k)
print(test)