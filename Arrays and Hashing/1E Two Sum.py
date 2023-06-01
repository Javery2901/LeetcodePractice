from typing import List

'''
Difficulty: Easy
Solution: Use a simple hash map to record the index and value of input list
Time complexity: O(n) n is the length of input list
Space complexity: O(n) n is the length of input list 
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]
            nums_dict[num] = i


s = Solution()
nums = [2, 7, 11, 15]
target = 9
res = s.twoSum(nums, target)
print(res)
