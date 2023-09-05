import collections
from typing import List
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = collections.Counter(nums)

        def backtracking(ls):
            if len(ls) == len(nums):
                res.append(ls[:])
                return
            for i in counter:
                if counter[i]:
                    ls.append(i)
                    counter[i] -= 1
                    backtracking(ls)
                    ls.pop()
                    counter[i] += 1
        backtracking([])
        return res


if __name__ == '__main__':
    s = Solution()
    nums=[1,2,3]
    print(s.permute(nums))