import collections
import heapq

from math import inf
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        AL = collections.defaultdict(list)
        for flight in flights:
            AL[flight[0]].append((flight[1], flight[2]))
        # {0: [(1, 100)], 1: [(2, 100), (3, 600)], 2: [(0, 100), (3, 200)]})
        node_stop = {i: float("inf") for i in range(n)}
        # important: we trace the stops, not cost
        if n == 1:
            return 0
        if not AL[src]:
            return -1

        pq = []
        heapq.heappush(pq, (0, src, -1))  # (cost, city, transfer_number)
        while pq:
            cost, u, stop = heapq.heappop(pq)
            if u == dst:
                return cost
            if stop >= min(k, node_stop[u]):
                continue
            # important step: skip current iteration if number of stops exceed maximun
            # or we have reached current node with fewer stops, supposing we've visited this node before
            # due to the heapq, we must have found a path with lower cost to this node before
            # The only reason we might want to visit it again is if we can visit it with fewer steps
            # so, if this is not the "fewer steps", skip
            node_stop[u] = stop
            for next_city in AL[u]:
                v, c = next_city[0], next_city[1]
                heapq.heappush(pq, (c + cost, v, stop + 1))
        return -1

    def findCheapestPrice_bfs(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [0 if i == src else -1 for i in range(n)]  # 用dict也可以
        al = collections.defaultdict(list)
        for u, v, price in flights:
            al[u].append((price, v))
        queue = collections.deque([src])
        step = 0
        while queue and step <= k:
            print(queue)
            print(cost)
            length = len(queue)
            temp_cost = cost.copy()
            for _ in range(length):
                node = queue.popleft()
                for price, neighbor in al[node]:
                    if temp_cost[neighbor] == -1 or temp_cost[neighbor] > cost[node] + price:
                        temp_cost[neighbor] = cost[node] + price
                        queue.append(neighbor)
            step += 1
            cost = temp_cost
        print(cost)
        return cost[dst]
s = Solution()
n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2
test = s.findCheapestPrice(n, flights,src,dst,k)
print(test)