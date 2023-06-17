import collections
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        AL = collections.defaultdict(list)
        for i in range(len(edges)):
            AL[edges[i][0]].append((edges[i][1], -succProb[i]))
            AL[edges[i][1]].append((edges[i][0], -succProb[i]))
        # print(AL)  # {0: [(1, 0.5), (2, 0.2)], 1: [(0, 0.5), (2, 0.5)], 2: [(1, 0.5), (0, 0.2)]})
        visited = set()
        pq = []
        prob = [-1 if i == start else 2 for i in range(n)]  # this is minheap
        heapq.heappush(pq, (-1, start))  # (probability, node)
        while pq:
            probabilty, u = heapq.heappop(pq)
            if u in visited or probabilty > prob[u]:
                continue
            visited.add(u)
            for v, p in AL[u]:
                if v in visited or -(p * probabilty) >= prob[v]:
                    continue
                prob[v] = -(p * probabilty)
                heapq.heappush(pq, (prob[v], v))
        if prob[end] == 2:
            return round(0, 5)
        return round(-prob[end], 5)




s = Solution()
n = 3
edges = [[0, 1]]
succProb = [0.5]
start = 0
end = 2
test = s.maxProbability(n, edges, succProb, start, end)
print(test)