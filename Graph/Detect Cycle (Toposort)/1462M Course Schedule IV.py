import collections
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # toposort
        # use a dict to store {course: {pre1, pre2, pre3....}}
        # space: O(n ^ 2)
        indegree = collections.defaultdict(int)
        course_map = {node: set() for node in range(numCourses)}
        for pre_course, course in prerequisites:
            course_map[pre_course].add(course)
            indegree[course] += 1

        pre_lookup = collections.defaultdict(set)
        queue = collections.deque([])
        for n in course_map:
            if indegree[n] == 0:
                queue.append(n)

        while queue:
            cur = queue.popleft()
            for neighbor in course_map[cur]:
                pre_lookup[neighbor].add(cur)
                pre_lookup[neighbor].update(pre_lookup[cur])  # update method

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        # now we have constructed a map

        res = [False] * len(queries)
        for i, query in enumerate(queries):
            pre_course, course = query[0], query[1]
            if pre_course in pre_lookup[course]:
                res[i] = True
        return res


s = Solution()
numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))