import collections
from typing import List
"""
相比较于 leetcode 78, 这道题需要额外的处理掉相同的subset
可在leetcode 78的基础上，添加一个集合，内部是排好序的sublist，从而确保不存在相同sublist
time complexity: O(n * (2 ^ n))
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sublist = []

        def dfs_backtracking(index):
            res.append(list(sublist))

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                sublist.append(nums[i])
                dfs_backtracking(i + 1)
                sublist.pop()

        dfs_backtracking(0)
        return res


s = Solution()
nums = [1, 2, 2]
test = s.subsetsWithDup(nums)
print(test)