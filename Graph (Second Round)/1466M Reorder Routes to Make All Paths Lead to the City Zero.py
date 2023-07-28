import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        indegree = collections.defaultdict(list)
        outdegree = collections.defaultdict(list)
        res = 0
        visited = set()
        for city in connections:
            i, j = city[0], city[1]
            outdegree[i].append(j)
            indegree[j].append(i)

        # outdegree， 0 -> 1, res += 1, 1 -> 3, res += 1, recursion,
        # visited = {0, 1, 3}，(0, 1, 3) can be considered as a whole
        # indegree， 0 -> 4, 1 -> 0 (continue), 3 -> 2, res does not change，recursion
        queue = collections.deque([0])
        while len(visited) < n:
            while queue:
                pop_node = queue.popleft()
                visited.add(pop_node)
                for i in indegree[pop_node]:
                    if i not in visited:
                        queue.append(i)  # indegree dict, means 4 -> 0, dont need to add
                        # then we can consider 4 and 0 as a whole, so add 4 to queue
                for i in outdegree[pop_node]:
                    if i not in visited:
                        res += 1
                        queue.append(i)  # outdegree dict, means 0 -> 1, need to add
                        # then we can consider 1 and 0 as a whole, so add 1 to queue
            # now visited = {0, 1, 3}
        return res

    def minReorder_stack(self, n: int, connections: List[List[int]]) -> int:
        # 出度，入度表
        # 先从入读表，加入所有0的入读表，因为0的入读表代表着所有直接连向0的点
        outdegree = collections.defaultdict(list)
        indegree = collections.defaultdict(list)
        for u, v in connections:
            outdegree[u].append(v)
            indegree[v].append(u)

        visited = {0}
        stack = [0]

        count = 0
        print(stack)
        while stack:
            pop_node = stack.pop()
            if pop_node in indegree:
                for neighbor in indegree[pop_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            if pop_node in outdegree:
                for neighbor in outdegree[pop_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        count += 1
            # print(stack, visited, count)
        return count


s = Solution()
n = 3
connections = [[1,0],[2,0]]
test = s.minReorder(n, connections)
print(test)

