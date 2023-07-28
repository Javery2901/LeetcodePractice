import collections
from typing import List


class Solution:
    def findCircleNum_dfs(self, isConnected: List[List[int]]) -> int:
        # try dfs first
        # redo the isConnected list, change it to dict
        al = collections.defaultdict(list)
        for i, cities in enumerate(isConnected):
            for j in range(len(cities)):
                if i == j or cities[j] == 0:
                    continue
                al[i].append(j)
        # print(al)  # {0: [1], 1: [0]}

        def dfs(city, visited):
            visited.add(city)
            for neighbor_city in al[city]:
                if neighbor_city not in visited:
                    dfs(neighbor_city, visited)

        res = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i, visited)
                res += 1
        return res

    def findCircleNum_UFS(self, isConnected: List[List[int]]) -> int:
        # try ufs
        # redo the isConnected list, make it to [[1], [0], []], index is the city
        graph = []
        for i, cities in enumerate(isConnected):
            ls = []
            for j in range(len(cities)):
                if i == j or cities[j] == 0:
                    continue
                ls.append(j)
            graph.append(ls)
        print(graph)  # [[1], [0], []]

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
            if x_parent == y_parent:
                return
            ls[x_parent] = y_parent
            return

        ls = [i for i in range(len(graph))]
        res = len(graph)
        # 总共有res个单独的城市，没发现一个可以union的，减去1，代表他俩被融合，那么最多变成res - 1 个省
        for city in range(len(graph)):
            for neighbor in graph[city]:
                if find(city, ls) != find(neighbor, ls):
                    union(city, neighbor, ls)
                    res -= 1
        return res


s = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
test = s.findCircleNum_UFS(isConnected)
print(test)