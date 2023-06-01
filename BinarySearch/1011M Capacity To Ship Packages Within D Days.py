"""
Difficulty: Median
Solution: binary search template
Time complexity: O(logn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):  # check if it can ship all within required days
            day = 1
            weight = 0
            for i in weights:
                weight += i
                if weight > capacity:
                    weight = i
                    day += 1
                    if day > days:
                        return False
            return True

        left, right = max(weights), sum(weights)
        # capacity: the minimum requirement is that it can ship at least one package
        # maximum requirement is that it can ship all packages in one day
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            print(feasible(mid))
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
            print(left, right)
        return left


sol = Solution()
weights = [1,2,3,1,1]
days = 4
res = sol.shipWithinDays(weights, days)
print(res)
