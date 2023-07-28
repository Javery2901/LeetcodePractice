"""
Spanning tree: a subgraph of G that is connected undirected weighted graph
Minimum spanning tree(mst) of G is a spanning tree that has the smallest total weight
The output is either the actual MST of G ot just the min total weight.

Kruskal's algorithm and Prim's algorithm: greedy algorithm
Time complexity: O(ElogV)

Kruskal's algorithm: 使用Edge list储存graph，使用并查集判断圈
原理：1. 将边以non-decreasing排列，如果两个边weight相同，则node较小的优先
     2. 对这些边进行循环，如果边不构成环，则贪心的取出并记录

Prim's algorithm: 从起始的源节点开始，贪心地扩张到整个图，
使用heapq记录最小权重边，使用AL存储graph节点，使用一个集合检查环
原理：1。 将起始点S的边和邻接节点（w，v）放入heapq中，然后开始循环操作
     2. 若v不在visited中，这意味着我们的树可以延伸到v。因此开始将v的边和邻接节点放入heapq中。
     3. 若v在visited中，则表明这条边是个环，continue
"""
import heapq
from typing import List


class UFDS:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.isSameSet(x, y):
            return
        x_parent = self.find(x)
        y_parent = self.find(y)
        self.p[x_parent] = y_parent


class MSTAlgorithm:
    def Kruskal(self, EL: List[tuple], node_number):
        # EL: (w, u, v)
        EL.sort()
        mst_cost = 0
        num_taken = 0
        uf = UFDS(num_taken)

        for i in range(node_number):
            if num_taken == node_number - 1:
                break
            w, u, v = EL[i]
            if not uf.isSameSet(u, v):
                num_taken += 1
                mst_cost += w
                uf.union(u, v)

        return mst_cost

    def prim(self, AL: List[List], node_number):
        # AL[u].append((v, w))
        # AL[v].append((u, w))
        visited = {0}  # assume we start from node 0
        qp = []
        for v, w in AL[0]:  # assume we start from node 0
            heapq.heappush(qp, (w, v))
        mst_cost = 0
        num_taken = 0

        while qp and num_taken < node_number - 1:
            w, u = heapq.heappop(qp)
            visited.add(u)
            num_taken += 1
            mst_cost += w
            for v, weight in AL[u]:
                if v not in visited:
                    heapq.heappush(qp, (weight, v))

        return mst_cost




