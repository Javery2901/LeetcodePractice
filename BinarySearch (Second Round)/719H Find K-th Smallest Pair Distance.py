from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def count(n): # sliding window
            res = 0
            l = 0
            for r in range(1, len(nums)):
                while l < r and nums[r] - nums[l] > n:
                    l += 1
                res += r - l
            return res >= k

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if count(mid):
                # if true, means there are more than k pairs if mid
                # means mid is too big
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
nums = [1,3,1]
k = 1
test = s.smallestDistancePair(nums, k)
print(test)