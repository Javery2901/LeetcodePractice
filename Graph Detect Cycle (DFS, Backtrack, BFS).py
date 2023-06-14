"""
以 leetcode 207 题为例，判断图是否包含圈
三种方法，图均以AL表记录。
time complexity: O(V + E)
"""
import collections


class Solution:
    def detect_cycle_dfs(self, node_number: int, AL: dict) -> bool:
        status = [0] * node_number

        # 0: unvisited, 1: exploring, 2: visited

        def dfs(node):
            status[node] = 1  # exploring
            if node in AL:
                for next_node in AL[node]:
                    if status[next_node] == 1:
                        return True
                    if status[next_node] == 0 and dfs(next_node):
                        return True
            # after the for loop, if the next_node has no cycle,
            # we come back and change the node status to visited
            status[node] = 2
            return False

        for node in range(node_number):
            # This for loop is to check all nodes, even if it is not in the AL
            if status[node] == 0:
                if dfs(node):
                    return True
        return False

    def detect_cycle_backtrack(self, node_number: int, AL: dict) -> bool:
        visited =set()
        # we dont need the exploring status anymore

        def backtrack(node):
            if node in visited:
                return True
            if node not in AL:
                return False

            visited.add(node)
            for next_node in AL[node]:
                if backtrack(next_node):
                    return True
            visited.remove(node)
            del AL[node]  # this is important to prevent duplicate computation

        for node in range(node_number):
            if backtrack(node):
                return True
        return False

    def detect_cycle_bfs(self, node_number: int, AL: dict) -> bool:
        indegree = [0] * node_number
        for k, v in AL.items():
            for indegree_node in v:
                indegree[indegree_node] += 1  # [0, 1, 1, 2]

        queue = collections.deque([])
        count = 0
        for i in range(node_number):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            pop_node = queue.popleft()
            count += 1
            if pop_node in AL:
                for next_node in AL[pop_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)

        if count < node_number:
            return True
        return False


s = Solution()
node_number = 4
AL = {0: [1, 2], 1: [3], 2: [3]}
test1 = s.detect_cycle_dfs(node_number, AL)
print(test1)
test2 = s.detect_cycle_backtrack(node_number, AL)
print(test2)
AL2 = {0: [1, 2], 1: [3], 2: [3]}
test3 = s.detect_cycle_bfs(node_number, AL2)
print(test3)
