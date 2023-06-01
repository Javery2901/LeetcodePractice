from typing import List

'''
Difficulty: Median
Solution: Use a set to contain all the numbers, find the smallest number in a consecutive sequence first
          and then start to count. 
Time complexity: O(n) 2*n
Space complexity: O(1)
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)  # O(n)
        max_num = 0

        for i in nums:
            k = 0
            if i not in nums_set or i - 1 in nums_set:
                continue
            if i - 1 not in nums_set:
                k += 1
                nums_set.discard(i)
                while i + 1 in nums_set:
                    k += 1
                    nums_set.discard(i + 1)
                    i += 1
            if max_num < k:
                max_num = k
        return max_num


s = Solution()
nums = [100,4,200,1,3,2]
res = s.longestConsecutive(nums)
print(res)