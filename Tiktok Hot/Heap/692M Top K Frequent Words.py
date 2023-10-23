import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # space complexity: O(n)
        # time complexity: O(3*n+klogn)
        # 时间复杂度相对来说可以接受，但是空间复杂度并不是最优
        # O(n)
        counts = collections.Counter(words)
        # O(n)
        ans = []
        for word, count in counts.items():
            ans.append((-count, word))
        # O(n)
        heapq.heapify(ans)
        # O(klogn)
        return [heapq.heappop(ans)[1] for _ in range(k)]


class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 最优解
        # time complexity：O(nlogk)
        # space complexity:O(n)

        # O(n)
        freq = collections.Counter(words)
        # O(nlogk)
        ans = []
        for word, count in freq.items():
            if len(ans) < k:
                heapq.heappush(ans, Pair(count, word),)
            else:
                heapq.heappushpop(ans, Pair(count, word))
        # O(klogk)
        return [node.word for node in sorted(ans, reverse=True)]


words = ["the","day","is","sunny","the","the","the","sunny","is","is","aaha"]
k = 4
test = Solution2()
print(test.topKFrequent(words, k))
