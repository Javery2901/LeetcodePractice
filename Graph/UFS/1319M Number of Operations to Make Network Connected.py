from typing import List


class Solution:
    def __init__(self):
        self.union_count = 0

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 并查集，找出有多少个分离的部分，则为答案
        if n - len(connections) > 1:  # 若有六个机器，最少需要5根线
            return -1

        def find(x, ls):
            if x == ls[x]:
                return x
            cur = x
            while cur != ls[cur]:
                cur = ls[cur]
            return cur

        def union(x, y, ls):
            x_parent = find(x, ls)
            y_parent = find(y, ls)
            if x_parent == y_parent:
                return
            ls[x_parent] = y_parent
            self.union_count += 1
            return

        ls = [i for i in range(n)]
        for computer1, computer2 in connections:
            union(computer1, computer2, ls)
            # union_count表示合并的次数
        return len(connections) - self.union_count


s = Solution()
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
test = s.makeConnected(n, connections)
print(test)