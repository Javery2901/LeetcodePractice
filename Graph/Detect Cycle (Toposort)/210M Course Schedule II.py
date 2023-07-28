import collections
from typing import List


class Solution:
    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        status = [0] * numCourses  # 0: unvisited, 1: exploring, 2: visited
        AL = collections.defaultdict(list)
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])

        def dedect_cycle(node, toposort):
            status[node] = 1
            for next_node in AL[node]:
                if status[next_node] == 1:
                    return True
                if status[next_node] == 0 and dedect_cycle(next_node, toposort):
                    return True
                if status[node] == 2:
                    continue
            status[node] = 2
            toposort.append(node)
            return False

        toposort = []
        for node in range(numCourses):
            if status[node] == 0:
                if dedect_cycle(node, toposort):
                    return []
        toposort.reverse()
        return toposort

    def findOrder_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        AL = collections.defaultdict(list)
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])
            indegree[edge[0]] += 1

        queue = collections.deque([])
        toposort = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0

        while queue:
            pop_node = queue.popleft()
            count += 1
            toposort.append(pop_node)
            for next_node in AL[pop_node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        if count < numCourses:
            return []
        return toposort

    def findOrder_backtrack(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AL = collections.defaultdict(list)
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])
        visited = set()
        toposort = []
        used = set()

        def dedect_cycle_backtrack(node):
            if node in visited:
                return True
            if node in used:
                return False
            visited.add(node)
            for next_node in AL[node]:
                if dedect_cycle_backtrack(next_node):
                    return True

            visited.remove(node)

            used.add(node)
            toposort.append(node)

        for i in range(numCourses):
            if dedect_cycle_backtrack(i):
                return []
        toposort.reverse()
        return toposort


s = Solution()
numCourses = 2
prerequisites = [[1,0]]
test = s.findOrder_dfs(numCourses, prerequisites)
print(test)
test2 = s.findOrder_bfs(numCourses, prerequisites)
print(test2)
test3 = s.findOrder_backtrack(numCourses, prerequisites)
print(test3)
