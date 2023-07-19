from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dic = {}
        for i, n in enumerate(nums):
            backet = n // (valueDiff + 1)
            if backet in dic and i - dic[backet][0] <= indexDiff:
                return True
            if backet - 1 in dic and i - dic[backet][0] <= indexDiff and abs(n - dic[backet - 1][1]) <= valueDiff:
                return True
            if backet + 1 in dic and i - dic[backet][0] <= indexDiff and abs(n - dic[backet + 1][1] <= valueDiff):
                return True
            dic[backet] = (i, n)
        return False


s = Solution()
nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0
test = s.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
print(test)