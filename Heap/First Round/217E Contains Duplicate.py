from heapq import heapify, heappush, heappop

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = nums
        heapify(self.hq)  # O(n)
        while len(self.hq) > k:
            heappop(self.hq)

    def add(self, val: int) -> int:
        if len(self.hq) < self.k:
            heappush(self.hq, val)
        elif val > self.hq[0]:
            heappop(self.hq)
            heappush(self.hq, val)
        return self.hq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)