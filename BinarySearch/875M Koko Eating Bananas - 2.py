"""
Difficulty: Median
Solution: binary search
Time complexity: O(nlogn)
Space complexity: O(1)
"""
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(capacity):
            hour = 0
            for i in piles:
                eat = i
                if eat <= capacity:
                    hour += 1
                else:
                    hour += ceil(eat / capacity)
                if hour > h:
                    return False
            return True

        start = 1
        end = max(piles)
        # the minimum is 1 if h >= max(piles), the maximum is max(piles) if h = 1
        while start < end:
            k = start + (end - start) // 2
            print(k)
            print(feasible(k))
            if feasible(k):
                end = k
            else:
                start = k + 1
            # print(ret, k, start, end)
            print(start, end)
        return start


sol = Solution()
piles = [3,6,7,11]
h = 8
res = sol.minEatingSpeed(piles, h)
print(res)