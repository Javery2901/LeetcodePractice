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


s = Solution()
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
test = s.openLock(deadends, target)
print(test)
