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


s = Solution()
nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,6]
k = 1
res = s.topKFrequent(nums, k)
print(res)