import collections
from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res =[]
        count = collections.Counter(words)
        ls = []
        for key, val in count.items():
            heapq.heappush(ls, (-val, key))
        for _ in range(k):
            pop_v, pop_k = heapq.heappop(ls)
            res.append(pop_k)
        return res


s = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
test = s.topKFrequent(words, k)
print(test)