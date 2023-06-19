import collections
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = collections.Counter(hand)
        pq = list(count.keys())
        heapq.heapify(pq)  # # O(n)
        while pq:
            smallest = pq[0]
            for num in range(smallest, smallest + groupSize):
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != pq[0]:
                        return False
                    heapq.heappop(pq)
        return True


s = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
test = s.isNStraightHand(hand, groupSize)
print(test)
