from typing import List
import collections

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = []
        count = collections.Counter(nums)

        def dfs_backtracking():
            if len(sublist) == len(nums):
                res.append(list(sublist))
                return
            for i in count:
                if count[i]:
                    sublist.append(i)
                    count[i] -= 1
                    dfs_backtracking()
                    sublist.pop()
                    count[i] += 1

        dfs_backtracking()
        return res


s = Solution()
nums = [1,2,3]
test = s.permuteUnique(nums)
print(test)