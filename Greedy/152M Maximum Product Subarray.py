"""
和 leetcode 53不同，53保存的是current_max 和全局max
这道题保存current_min 和 current_max， 因为整数乘积不会出现越来越小的情况，只有正负号
但同时需要考虑 n == 0 的情况
因此每一轮会出现三个值，一个是n本身，一个是n*之前最大的值（最大值可以想象为没有负号或者有两个负号）
最后一个为n*之前最小值，因为有可能最小值*n就变成最大值
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_min, current_max = nums[0], nums[0]
        res = nums[0]
        for n in nums[1:]:
            vals = (n, n * current_max, n * current_min)
            current_max = max(vals)
            current_min = min(vals)
            res = max(res, current_max)
        return res


s = Solution()
nums = [3,-1,4]
test = s.maxProduct(nums)
print(test)