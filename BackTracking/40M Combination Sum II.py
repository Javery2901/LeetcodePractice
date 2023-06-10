import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sublist = []

        def dfs_backtracking(index, combine_sum):
            if combine_sum == target:
                res.append(list(sublist))
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + combine_sum <= target:
                    sublist.append(candidates[i])
                    dfs_backtracking(i + 1, candidates[i] + combine_sum)
                    sublist.pop()
                else:
                    break

        dfs_backtracking(0, 0)
        return res


s = Solution()
candidates = [2,5,2,1,2]
target = 5
test = s.combinationSum2(candidates, target)
print(test)