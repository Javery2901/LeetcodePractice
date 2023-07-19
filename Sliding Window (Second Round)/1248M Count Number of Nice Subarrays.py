from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # idea: we want a subarray with exactly k odd numbers
        # using sliding window, what we can do is to return a subarray with smaller than or equal to k odd numbers
        # in this way, we can return the number of subarray that has just or less than k odd numbers
        # and we can return the number of subarray that has just or less than k - 1 odd numbers
        # then we have No. of <= k - No. of <= k- 1  --> just k
        def less_than_or_equal_to(target):
            left = 0
            count = 0
            res = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    count += 1
                while count > target:  # it is ok when count is smaller than or equal to target
                    if nums[left] % 2 == 1:
                        count -= 1
                    left += 1
                res += right - left + 1  # important,
                # we are adding the new outcomes that the subarray is ending at index right
            print(res)
            return res
        return less_than_or_equal_to(k) - less_than_or_equal_to(k - 1)

    def numberOfSubarrays_prefix_sum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        count = res = 0
        for i, num in enumerate(nums):
            # print(i, num)
            if num % 2 == 1:
                count += 1
            if count - k in dic:
                res += dic[count - k]
            dic[count] = dic.get(count, 0) + 1
            # print(dic, res)
        return res


s = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
test = s.numberOfSubarrays_prefix_sum(nums, k)
print(test)