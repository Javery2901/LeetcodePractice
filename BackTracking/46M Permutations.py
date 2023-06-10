import collections
from typing import List
"""
time complexity: O(n ^ n)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = []
        count = collections.Counter(nums)

        def dfs():
            if len(sublist) == len(nums):
                res.append(list(sublist))
                return
            for i in count:
                if count[i]:
                    sublist.append(i)
                    count[i] -= 1
                    dfs()
                    sublist.pop()
                    count[i] += 1
        dfs()
        return res


s = Solution()
nums = [1,2,3]
test = s.permute(nums)
print(test)