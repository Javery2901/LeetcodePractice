import collections
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 先创造al，红色为1， 蓝色为-1
        al = collections.defaultdict(list)
        for i, j in blueEdges:
            al[i].append((j, 1))
        for i, j in redEdges:
            al[i].append((j, -1))
        print(al)  # {1: [(2, 1), (2, -1)], 2: [(3, 1), (3, -1)], 3: [(1, 1), (4, -1)], 0: [(1, -1)]}
        res = [0 if i == 0 else -1 for i in range(n)]
        # print(res)  # [0, -1, -1]
        # bfs, start from 0, level by level
        queue = collections.deque([(0, 0, 0)])  # (node, color, step)
        visited = {(0, 0)}  # 因为有平行或者自己指向自己的可能性，因此需要加入颜色控制
        while queue:
            node, color, step = queue.popleft()
            for neighbor, neighbor_color in al[node]:
                if (neighbor, neighbor_color) in visited:
                    continue
                if color == 0 or neighbor_color != color:  # start from zero
                    if res[neighbor] == -1:  # 如果已经有了，根据bfs最短距离原理，不需要再改变
                        res[neighbor] = step + 1
                    queue.append((neighbor, neighbor_color, step + 1))
                    visited.add((neighbor, neighbor_color))
        return res


s = Solution()
n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]
print(s.shortestAlternatingPaths(n, redEdges, blueEdges))