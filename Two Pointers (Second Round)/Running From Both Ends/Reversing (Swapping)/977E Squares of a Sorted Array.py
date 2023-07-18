from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1

        return res


s = Solution()
nums = [-7,-3,2,3,11]
test = s.sortedSquares(nums)
print(test)