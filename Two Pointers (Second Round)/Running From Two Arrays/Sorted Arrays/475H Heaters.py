from cmath import inf
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # [1,2,3,4,5,8,10]
        # [-inf, 1,4,7,inf]
        # idea: everytime we compare the distance between (houses[i] to heaters[j] and hoses[i] to heaters[j + 1]
        # where heaters[j] <= houses[i] and heaters[j + 1] >= houses[i]
        houses.sort()
        heaters.sort()
        heaters = [-inf] + heaters + [inf]  # O(n)
        res = 0
        pos = 0
        for house in houses:
            while heaters[pos] < house:
                pos += 1
            radius = min(house - heaters[pos - 1], heaters[pos] - house)
            res = max(res, radius)
        return res


s = Solution()
houses = [1,2,3,4]
heaters = [1,4]
test = s.findRadius(houses, heaters)
print(test)
