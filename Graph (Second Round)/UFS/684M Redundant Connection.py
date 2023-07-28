import collections
from typing import List


class UFDS:
    def __init__(self, size):
        self.parent = list(range(size + 1))

    def find(self, x):
        cur = x
        while cur != self.parent[cur]:
            cur = self.parent[cur]
        return cur

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return True
        self.parent[x_parent] = y_parent
        return


class Solution:
    def findRedundantConnection_UFS(self, edges: List[List[int]]) -> List[int]:
        ufds = UFDS(len(edges))
        for edge in edges:
            if ufds.union(edge[0], edge[1]):
                return [edge[0], edge[1]]


s = Solution()
edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
test = s.findRedundantConnection_UFS(edges)
print(test)
