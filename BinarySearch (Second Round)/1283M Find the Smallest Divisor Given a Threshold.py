from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # divisor maximum: max(nums)
        # divisor minimum: 1

        def division(n):
            res = 0
            for i in nums:
                res += i // n
                if i % n != 0:
                    res += 1
            return res <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if division(mid):
                # if True, means the division's result is smaller than threshold
                # means mid is too big
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
nums = [1, 2, 5, 9]
threshold = 7
test = s.smallestDivisor(nums, threshold)
print(test)