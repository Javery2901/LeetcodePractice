import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和思想，每次都加上前面，如果与k的差为0，则说明匹配
        dic = collections.defaultdict(int)
        dic[0] = 1
        res = 0
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in dic:
                # print(prefix_sum)
                res += dic[prefix_sum - k]
            dic[prefix_sum] += 1
        # print(dic)
        return res


s = Solution()
nums = [1,2,3]
k = 3
print(s.subarraySum(nums, k))
