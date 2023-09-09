from typing import List
"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，
并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。
如果至少一个数字的被选数量不同，则两种组合是不同的。 

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sublist = []

        def dfs_backtracking(index, combine_sum):
            if combine_sum == target:
                res.append(list(sublist))
                return

            for i in range(index, len(candidates)):
                if candidates[i] + combine_sum <= target:
                    sublist.append(candidates[i])
                    dfs_backtracking(i, candidates[i] + combine_sum)
                    sublist.pop()
                else:
                    break

        dfs_backtracking(0, 0)
        return res


s = Solution()
candidates = [2,3,6,7]
target = 7
test = s.combinationSum(candidates, target)
print(test)