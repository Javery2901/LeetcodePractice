from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # minimum capacity is min(weights)
        # maximum capacity is sum(weights)
        left = max(weights)
        right = sum(weights)

        def capacity(n):
            day = 1
            load = 0
            for w in weights:
                if load + w <= n:
                    load += w
                else:
                    day += 1
                    load = w
            if day <= days:
                return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if capacity(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
weights = [3,2,2,4,1,4]
days = 3
test = s.shipWithinDays(weights, days)
print(test)