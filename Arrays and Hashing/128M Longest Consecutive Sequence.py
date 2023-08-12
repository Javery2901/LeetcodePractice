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

    def longestConsecutive_0812(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)

        for i in nums:
            if i in nums_set and i - 1 in nums_set:
                continue  # we need to find the smallest first
            if i in nums_set and i - 1 not in nums_set:  # i is the smallest one
                temp_max_length = 1
                nums_set.remove(i)
                while i + 1 in nums_set:
                    temp_max_length += 1
                    nums_set.remove(i + 1)
                    i += 1
                max_length = max(max_length, temp_max_length)

        return max_length


s = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
res = s.longestConsecutive_0812(nums)
print(res)