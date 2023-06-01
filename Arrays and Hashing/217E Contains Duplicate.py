from typing import List

'''
Difficulty: Easy
Solution: Use a simple hash map
Time complexity: O(n) n is the length of input list
Space complexity: O(n) n is the length of input list 
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
s = Solution()
res = s.containsDuplicate(nums)
print(res)
