import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            heapq.heappush(hq, -n)
        while k > 1:
            heapq.heappop(hq)
            k -= 1
        return -hq[0]
