import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # use bfs, every time there are 8 choices, push them into queue if any choice is valid
        dead = set(deadends)
        visited = set()
        if target == '0000':
            return 0
        if '0000' in dead:
            return -1
        queue = collections.deque()
        queue.append(('0000', 0))
        while queue:
            pop_node, lvl = queue.popleft()
            if pop_node in visited:
                continue
            visited.add(pop_node)

            # find the neighbor
            neighbor = []
            for i in range(4):
                neighbor.append(pop_node[:i] + str((int(pop_node[i]) + 1) % 10) + pop_node[i + 1:])
                neighbor.append(pop_node[:i] + str((int(pop_node[i]) - 1) % 10) + pop_node[i + 1:])

            # push the neighbor into queue if valid
            for neighbor_node in neighbor:
                if neighbor_node in dead:
                    continue
                if neighbor_node == target:
                    return lvl + 1
                queue.append((neighbor_node, lvl + 1))
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        # use bfs, every round there are 8 neighbors
        # cannot use dfs, if use bfs, actually it is backtracking, TLE
        queue = collections.deque(['0000'])
        dead = set(deadends)
        count = -1
        visited = {'0000'}
        if '0000' in dead:
            return -1
        while queue:
            count += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                # print(curr)
                if curr == target:
                    return count
                # find neighbor
                neighbor_list = []
                for i in range(4):
                    neighbor_list.append(curr[: i] + str((int(curr[i]) - 1) % 10) + curr[i + 1:])
                    neighbor_list.append(curr[: i] + str((int(curr[i]) + 1) % 10) + curr[i + 1:])
                for neighbor in neighbor_list:
                    if neighbor not in visited and neighbor not in dead:
                        queue.append(neighbor)
                        visited.add(neighbor)
        if not queue:
            return -1
s = Solution()
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
test = s.openLock(deadends, target)
print(test)
