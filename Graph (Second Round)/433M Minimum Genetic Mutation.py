import collections
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        # use bfs, dfs can not
        queue = collections.deque()
        visited = set()
        queue.append((startGene, 0))
        while queue:
            pop_gene, lvl = queue.popleft()
            if pop_gene in visited:
                continue
            visited.add(pop_gene)
            # find all the neighbors
            neighbors = []
            for i in range(len(pop_gene)):
                for j in ('A', 'C', 'G','T'):
                    neighbors.append(pop_gene[:i] + j + pop_gene[i + 1:])
            # check valid neighbor
            for neighbor_node in neighbors:
                if neighbor_node not in bank_set or neighbor_node in visited:
                    continue
                if neighbor_node == endGene:
                    return lvl + 1
                queue.append((neighbor_node, lvl + 1))
        return -1


s = Solution()
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
test = s.minMutation(startGene, endGene, bank)
print(test)