import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AL = collections.defaultdict(list)
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])  # {0: [1, 2], 1: [3], 2: [3]}
        # next step is to check if the graph is cyclic, dfs AL
        status = [0] * numCourses
        # record the status of nodes, 0: unvisited, 1: exploring, 2:visited

        def dfs_detected_cyclic(node, status):
            status[node] = 1 # exploring
            for neighbor_node in AL[node]:
                if status[neighbor_node] == 1:
                    return True  # if neighbor_node is under exploring, we declare that this is cyclic
                if status[neighbor_node] == 0 and dfs_detected_cyclic(neighbor_node, status):
                    return True
            status[node] = 2  # explore all the neighbors, if not cyclic yet, change the status of node: visited
            return False

        for i in range(numCourses):  # dont for loop al
            if status[i] == 0: # unvisited, start to dfs
                if dfs_detected_cyclic(i, status):  # dfs(), if cyclic, return True, else return False
                    return False
        return True

    def canFinish_backtrack(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AL = collections.defaultdict(list)
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])
        visited = set()

        def dfs_backtrack(node):  # check if it is cyclic
            if node in visited:
                return True
            if not AL[node]:
                return False
            visited.add(node)
            for next_node in AL[node]:
                if dfs_backtrack(next_node):
                    return True
            visited.remove(node)
            del AL[node]  # important

        for node in range(numCourses):
            if dfs_backtrack(node):
                return False
        return True

    def canFinish_bfs_indegree(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AL = collections.defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            AL[edge[1]].append(edge[0])
            indegree[edge[0]] += 1

        queue= collections.deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            pop_node = queue.popleft()
            numCourses -= 1
            for next_node in AL[pop_node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        if numCourses == 0:
            return True
        return False


s = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
test = s.canFinish(numCourses, prerequisites)
print(test)
test2 = s.canFinish_backtrack(numCourses, prerequisites)
print(test2)
test3 = s.canFinish_bfs_indegree(numCourses, prerequisites)
print(test3)
