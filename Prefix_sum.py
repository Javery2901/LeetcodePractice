"""
前缀和，以leetcode 560和 1248为例，
1248同时也可以用sliding window中的less than or equal to 解法，但sliding window要求整个数组必须是正整数

    # 前缀和的精髓，若遍历过程中，其和不等于target时，先不扔掉，用字典保存起来
    # [1,0,2,1] k = 3
    # adict = {1: 2, 3: 1} 当1 + 2 = 3时，字典中表示和为3的个数有1个
    # 当prefix_sum为4时， 4 - k == 1, 查看adict[1]存在与否
    # 若存在，含义：在加到4之前有，2个前缀和加到了1，那么抛弃这2个前缀和为1的子数组，剩余子数组的和就是k
    # 理解：何为1的子数组被抛弃，那么到4时，剩余子数组的和为3，即k。这种组合有adict[1]个
"""
# leetcode 556
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1,1,1,1,1,1,1,1,1,1,1,1] 前缀和：每次只能知道第0到第1，2，3，。。。10等的和是多少，
        # 但是并不知道从第3到第10的总和是多少，若想知道3-10的总和，可以用1-10的总和减去1-3的总和，即为3-10子数组的总和
        dic = {0: 1}  # 需要手动将和为0的数量定为1
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in dic:
                res += dic[prefix_sum - k]
            dic[prefix_sum] = dic.get(prefix_sum, 0) + 1
        return res


s = Solution()
nums = [-1,-1,1]
k = 0
test = s.subarraySum(nums, k)
print(test)