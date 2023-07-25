from typing import List


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