import collections
import heapq

from cmath import inf
from typing import List


class Solution:
    def maxProbability_modified(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # 这道题依然可以使用modified_dijkstra, 只是他是相乘，且是无向图，且是小数，输出最大值
        # 好处：由于要求输出最大值，我们需要使用minheap，即将所有权重添加负号
        # 由于是小数，越乘越小，即在minheap中越乘越大，而我们要的是尽可能小的值（负数），因此正好符合
        # 也不需要担心环的题，因为是负小数越乘越大，因此我们不会选择
        # 即当我们遍历完全后，probability中都将存储最小的负数，反过来即为每个点最大的概率
        probability = [-1 if i == start_node else 0 for i in range(n)]  # -1， 即start_node概率为1，最大
        # 由于是小数，越乘越小，而需要输出的是尽可能大的值，因此负向
        al = collections.defaultdict(list)
        for i, nodes in enumerate(edges):
            u, v = nodes[0], nodes[1]
            al[u].append((-succProb[i], v))
            al[v].append((-succProb[i], u))
        # print(al)  # {0: [(-0.5, 1), (-0.2, 2)], 1: [(-0.5, 0), (-0.5, 2)], 2: [(-0.5, 1), (-0.2, 0)]}
        hp = []
        heapq.heappush(hp, (-1, start_node))  # (weight, node)
        while hp:
            prob, node = heapq.heappop(hp)
            # 因为是负数，所以当prob越小，越贴近-1，实际越是我们需要的
            if prob > probability[node]:
                continue
            for neighbor_prob, neighbor in al[node]:
                if -1 * probability[node] * neighbor_prob >= probability[neighbor]:
                    continue  # 注意-1 *
                probability[neighbor] = -1 * probability[node] * neighbor_prob
                heapq.heappush(hp, (probability[neighbor], neighbor))
        # print(probability)
        return -probability[end_node]

    def maxProbabilit(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # 用普通dijkstra应该也可以
        al = collections.defaultdict(list)
        for i, nodes in enumerate(edges):
            u, v = nodes[0], nodes[1]
            al[u].append((-succProb[i], v))
            al[v].append((-succProb[i], u))
        # print(al)  # {0: [(-0.5, 1), (-0.2, 2)], 1: [(-0.5, 0), (-0.5, 2)], 2: [(-0.5, 1), (-0.2, 0)]}
        hq = []
        heapq.heappush(hq, (-1, start_node))  # (weight, node)
        visited = set()
        while hq:
            prob, node = heapq.heappop(hq)
            print(prob, node)
            if node == end_node:
                return -prob
            visited.add(node)
            for neighbor_prob, neighbor in al[node]:
                if neighbor not in visited:
                    heapq.heappush(hq, (-1 * neighbor_prob * prob, neighbor))
        return 0


s = Solution()
n = 3
edges = [[0,1]]
succProb = [0.5]
start_node = 0
end = 2
test = s.maxProbabilit(n, edges, succProb, start_node, end)
print(test)
