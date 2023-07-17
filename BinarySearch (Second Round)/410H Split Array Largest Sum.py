from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # minimum result is max(nums)
        # maximum result is sum(nums)
        # can use binary search indeed

        def largest_sum(n):
            num_of_subarray = 1
            sum_of_subarray = 0
            for i in nums:
                if sum_of_subarray + i <= n:
                    sum_of_subarray += i
                else:
                    num_of_subarray += 1
                    sum_of_subarray = i
            if num_of_subarray <= k:
                # when result = n, we can split the nums into <= k groups, which means n is too big
                return True
            return False

        left = max(nums)
        right =sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if largest_sum(mid):
                # mid is too big
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
nums = [7,2,5,10,8]
k = 2
test = s.splitArray(nums, k)
print(test)