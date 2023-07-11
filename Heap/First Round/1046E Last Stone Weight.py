from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x, y, stones)
            if x != y:
                heapq.heappush(stones, x - y)
        if stones:
            return -stones[0]
        return 0


s = Solution()
stones = [1]
test = s.lastStoneWeight(stones)
print(test)