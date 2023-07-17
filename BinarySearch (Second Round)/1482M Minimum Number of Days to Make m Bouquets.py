from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def bouquets(day):
            num_bouquets = 0
            adjacent = k
            for i in bloomDay:
                if i <= day:
                    adjacent -= 1
                    if adjacent == 0:
                        num_bouquets += 1
                        adjacent = k
                else:
                    adjacent = k
            return num_bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if bouquets(mid):
                right = mid
            else:
                left = 1 + mid
        return left


s = Solution()
bloomDay = [7,7,7,7,12,7,7,13]
m = 2
k = 4
test = s.minDays(bloomDay, m, k)
print(test)
