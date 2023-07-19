"""
Difficulty: Hard
Solution: Sliding Window
Time complexity: O()
Space complexity: O()
"""
from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def less_equal_k(nums, k):
            start = 0
            adict = defaultdict(int)
            count = 0
            for end in range(len(nums)):
                adict[nums[end]] += 1
                while len(adict) > k:
                    adict[nums[start]] -= 1
                    if adict[nums[start]] == 0:
                        del adict[nums[start]]
                    start += 1
                count += end - start + 1  # this is important
            return count
        return less_equal_k(nums, k) - less_equal_k(nums, k - 1)


sol = Solution()
nums = [1,2,1,3,4]
k = 3
res = sol.subarraysWithKDistinct(nums, k)
print(res)