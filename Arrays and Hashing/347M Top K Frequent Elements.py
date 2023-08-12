import collections
import heapq
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

'''
Difficulty: Median
Solution: Use a default-dict to count the frequency of numbers, then reverse  
          key and value, use a min heap queue to pop k most frequent elements
Time complexity: O(n + logn + klogn), n + n + logn + klogn, n is the length of input list, k is the input frequency.
Space complexity: O(n), 3 * n, n is the length of input list
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        # print(dic)
        reverse_dict = defaultdict(list)
        for key, v in dic.items():
            reverse_dict[v].append(key)
        hq = []
        for key in reverse_dict:
            heappush(hq, -key)
        ls = []
        while k > 0:
            key = heappop(hq)
            for i in reverse_dict[-key]:
                ls.append(i)
                k -= 1
        return ls

    def topKFrequent_0811(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ls = []
        for key, value in counter.items():  #
            ls.append((value, key))  # [(-freq, num)]
        res = []
        for i in range(len(ls)):
            if k == 0:
                if ls[i][0] > res[0][0]:
                    heapq.heappop(res)
                    k += 1
                else:
                    continue
            heapq.heappush(res, ls[i])
            k -= 1
        # print(res)
        return [number for freq, number in res]


s = Solution()
nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,6]
k = 2
res = s.topKFrequent_0811(nums, k)
print(res)