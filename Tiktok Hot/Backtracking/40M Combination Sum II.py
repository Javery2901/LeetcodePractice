import collections
from typing import List
"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

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
                if i > index and candidates[i] == candidates[i - 1]:  # important
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