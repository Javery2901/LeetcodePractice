from cmath import inf
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # dfs, 将两个node分别经过的每个点，以及到那个点的距离保存起来
        node1_dict = {}
        node2_dict = {}

        def dfs(node, distance, node_dict):
            node_dict[node] = distance
            if edges[node] == -1 or edges[node] in node_dict:
                return
            dfs(edges[node], distance + 1, node_dict)

        dfs(node1, 0, node1_dict)
        print(node1_dict)
        dfs(node2, 0, node2_dict)
        print(node2_dict)
        min_res = (inf, inf)  # (node, max_distance)
        for i in node1_dict:
            if i in node2_dict:
                max_distance = max(node1_dict[i], node2_dict[i])
                if min_res[1] > max_distance:
                    min_res = (i, max_distance)
                elif min_res[1] == max_distance:
                    min_res = (min(i, min_res[0]), max_distance)

        if min_res[0] == inf:
            return -1
        return min_res[0]


s = Solution()
edges = [4,4,4,5,1,2,2]
node1 = 1
node2 = 1
print(s.closestMeetingNode(edges, node1, node2))