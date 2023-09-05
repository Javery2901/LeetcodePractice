import collections
from typing import List
import heapq


class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count_words = collections.Counter(words)
        pq = []

        for word, count in count_words.items():
            heapq.heappush(pq, WordCount(word, count))
            if len(pq) > k:
                heapq.heappop(pq)

        res = []
        while pq:
            wordcount = heapq.heappop(pq)
            res.append(wordcount.word)

        return res[::-1]

        # count = Counter(words)
        # heap = [(-freq, word) for word, freq in count.items()]
        # heapq.heapify(heap)
        #
        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])
        #
        # return result


s = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 3
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
test = s.topKFrequent(words, k)
print(test)