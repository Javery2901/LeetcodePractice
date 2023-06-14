"""
适用于undirected graph 中的圈查找
"""


class UFDS:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        cur = x
        children = []
        while cur != self.parent[cur]:
            children.append(cur)
            cur = self.parent[cur]

        for c in children:  # 此步骤为压缩步骤，将路径上所有的子节点都直接连接到root
            self.parent[c] = cur
        return cur

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return
        self.parent[x_parent] = y_parent
        return


ufds = UFDS(8)
print(ufds.find(0))  # 0
print(ufds.parent)  # [0, 1, 2, 3, 4, 5, 6, 7]
ufds.union(0, 1)
print(ufds.parent)  # [1, 1, 2, 3, 4, 5, 6, 7]
ufds.union(0, 2)
print(ufds.parent)  # [1, 2, 2, 3, 4, 5, 6, 7]
print(ufds.find(0))  # 2
print(ufds.parent)  # [2, 2, 2, 3, 4, 5, 6, 7]
