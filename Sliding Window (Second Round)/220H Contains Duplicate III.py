from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dic = {}  # {backet1: (index, number)}
        for i, n in enumerate(nums):
            backet = n // (valueDiff + 1)  # 倍数区间
            print(i, n, backet)
            # 如果在同一个倍数区间内，则直接判断是否符合index要求
            if backet in dic and i - dic[backet][0] <= indexDiff:
                return True
            # 如果有一个小的倍数区间存在，则判断小的倍数区间和i，n是否符合index和value要求
            if backet - 1 in dic and i - dic[backet - 1][0] <= indexDiff and abs(n - dic[backet - 1][1]) <= valueDiff:
                return True
            # 如果有一个大的倍数区间存在，则判断大的倍数区间和i，n是否符合index和valueyaoqiu
            if backet + 1 in dic and i - dic[backet + 1][0] <= indexDiff and abs(n - dic[backet + 1][1]) <= valueDiff:
                return True
            dic[backet] = (i, n)
            # 每个倍数值保存的是最新的i，n
        return False


s = Solution()
nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3
test = s.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
print(test)