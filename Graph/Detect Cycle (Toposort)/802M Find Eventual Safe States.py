from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0: unvisited, 1:exploring, 2: visited
        # dfs过程中，如果中途发现某个node是环，将其标记并返回。并且这个dfs链条过程中的所有node都是环的一部分
        status = [0] * len(graph)
        res = []

        def cycle_detect(node):
            status[node] = 1  # exploring
            for neighbor in graph[node]:
                if status[neighbor] == 2:
                    continue
                elif status[neighbor] == 1:
                    return
                else:  # neighbor is not explored
                    cycle_detect(neighbor)
                    if status[neighbor] == 1:
                        return
            status[node] = 2
            return

        for node in range(len(graph)):  # 0 - n - 1
            if status[node] == 0:
                cycle_detect(node)
        # print(status)  # [1, 1, 2, 1, 2, 2, 2]
        for i in range(len(graph)):
            if status[i] != 1:
                res.append(i)
        return res


s = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
test = s.eventualSafeNodes(graph)
print(test)