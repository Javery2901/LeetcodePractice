from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        one_count = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                one_count += 1
            if right - left + 1 - one_count > k:
                while nums[left] == 1:
                    one_count -= 1
                    left += 1
                left += 1
            res = max(res, right - left + 1)
        return res


s = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
test = s.longestOnes(nums, k)
print(test)
