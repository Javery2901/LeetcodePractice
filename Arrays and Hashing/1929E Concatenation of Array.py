from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

s = Solution()
nums = [1,2,3,1]
test = s.getConcatenation(nums)
print(test)