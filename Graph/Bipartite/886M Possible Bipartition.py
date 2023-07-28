import collections
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # bipartite
        # construct al first
        al = collections.defaultdict(list)
        for i, j in dislikes:
            al[i].append(j)
            al[j].append(i)
        # print(al)  # {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}

        color = {}
        for node in al:
            queue = collections.deque()
            if node not in color:
                color[node] = 1
                queue.append(node)
            while queue:
                pop_node = queue.popleft()
                for neighbor in al[pop_node]:
                    if neighbor in color:
                        if color[neighbor] == color[pop_node]:
                            return False
                    else:
                        color[neighbor] = color[pop_node] * -1
                        queue.append(neighbor)
        return True


s = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
test = s.possibleBipartition(n, dislikes)
print(test)