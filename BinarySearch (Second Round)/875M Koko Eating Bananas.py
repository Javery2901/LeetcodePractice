from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time_require(speed):
            total_hour = 0
            for i in piles:
                if i <= speed:
                    total_hour += 1
                else:
                    total_hour += (i // speed)
                    if i % speed != 0:
                        total_hour += 1
            if total_hour <= h:
                # means speed is too fast
                return True
            return False

        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if time_require(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
piles = [30,11,23,4,20]
h = 5
test = s.minEatingSpeed(piles, h)
print(test)