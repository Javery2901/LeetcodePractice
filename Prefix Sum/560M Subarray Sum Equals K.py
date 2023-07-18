from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        prefix_sum = 0
        res = 0
        for num in nums:

            prefix_sum += num
            print(num, prefix_sum - k)
            if prefix_sum - k in dic:
                res += dic[prefix_sum - k]
                print(res)
            dic[prefix_sum] = dic.get(prefix_sum, 0) + 1
            print(dic)
        return res


s = Solution()
nums = [-1,-1,1]
k = 0
test = s.subarraySum(nums, k)
print(test)