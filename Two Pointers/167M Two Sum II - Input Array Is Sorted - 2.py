"""
Runtime: ms141, beat 27%
Difficulty: Median
Solution: two pointers
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1


sol = Solution()
numbers = [2,7,11,15]
target = 9
res = sol.twoSum(numbers, target)
print(res)
