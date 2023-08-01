from cmath import inf
from typing import List
"""
# 这个问题本质上类似leetcode 416， 当两组重量尽可能相等时，结果最小，即尽量等分两组的重量
# 01背包问题，每个元素只能用一次。
# 背包长度：sum // 2
"""

class Solution:
    def lastStoneWeightII_top_down(self, stones: List[int]) -> int:
        memo = {}

        def recursion(index, weight):
            if index == len(stones):
                if weight >= 0:
                    return weight
                else:
                    return inf
            if (index, weight) in memo:
                return memo[(index, weight)]
            memo[(index, weight)] = min(recursion(index + 1, weight - stones[index]),
                                        recursion(index + 1, stones[index] + weight))
            return memo[(index, weight)]

        res = recursion(0, 0)
        return res

    def lastStoneWeightII_bottom_up(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        # 构建一个表格，纵列是target，横行是index
        table = [0] * (target + 1)

        for stone in stones:
            for j in range(target, stone - 1, -1):
                table[j] = max(table[j], table[j - stone] + stone)
        return sum(stones) - 2 * table[-1]


s = Solution()
stones = [31,26,33,21,40]
test = s.lastStoneWeightII_top_down(stones)
print(test)