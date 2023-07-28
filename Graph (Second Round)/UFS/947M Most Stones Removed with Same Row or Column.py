import collections
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 若面试中遇到这种题，比较难第一时间想到并查集
        # 如果两个点在同一水平或者同一纵队，可以用并查集将他们连接，这样他们变成一个总体
        # 最后有几个总体，即有几个石头剩余
        ls = [i for i in range(len(stones))]

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
            return

        # use two dict to record x-axis and y-axis
        x_dict = collections.defaultdict(list)  # (x-axis: stone index)
        y_dict = collections.defaultdict(list)
        for stone_index, coordinate in enumerate(stones):
            row, col = coordinate[0], coordinate[1]
            if row in x_dict or col in y_dict:  # this means they have the same x-axis or y-axis, union
                if row in x_dict:
                    union(stone_index, x_dict[row][0], ls)
                if col in y_dict:
                    union(stone_index, y_dict[col][0], ls)
            # append to the dict list
            x_dict[row].append(stone_index)
            y_dict[col].append(stone_index)

        # at last, traverse the ls, count the number of x == ls[x], that is the final answer
        res = 0
        for i in range(len(ls)):
            if i == ls[i]:
                res += 1
        return len(stones) - res


s = Solution()
stones = [[0,0]]
test = s.removeStones(stones)
print(test)