"""
Runtime: ms248, beat %6
Difficulty: Median
Solution: binary search, clearly not optimal
Time complexity: O(nlogn)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            start = i
            end = len(numbers) - 1
            while start <= end:
                j = (start + end) // 2
                # print(i, j)
                if target - numbers[i] == numbers[j]:
                    if i == j:
                        end += 1
                    else:
                        return [i + 1, j + 1]
                elif target - numbers[i] < numbers[j]:
                    end = j - 1
                else:
                    start = j + 1


sol = Solution()
numbers = [2,7,11,15]
target = 9
res = sol.twoSum(numbers, target)
print(res)
