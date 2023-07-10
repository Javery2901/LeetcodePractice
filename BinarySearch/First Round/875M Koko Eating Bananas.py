"""
Runtime: ms488, beat 44%
Difficulty: Median
Solution: binary search
Time complexity: O(nlogn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            k = (start + end) // 2
            ret = 0
            for i in piles:
                ret += i // k + 1 if i % k > 0 else i // k
            if ret <= h:
                end = k
            else:
                start = k + 1
            # print(ret, k, start, end)
        return start


sol = Solution()
piles = [3,6,7,11]
h = 8
res = sol.minEatingSpeed(piles, h)
print(res)