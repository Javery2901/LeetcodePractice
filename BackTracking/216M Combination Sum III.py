from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sublist =[]
        res = []

        def dfs_backtracking(index, combine_sum):
            if len(sublist) == k and combine_sum == n:
                res.append(list(sublist))
                return

            for i in range(index, 10):
                if i + combine_sum <= n:
                    sublist.append(i)
                    dfs_backtracking(i + 1, i + combine_sum)
                    sublist.pop()
                else:
                    break

        dfs_backtracking(1, 0)
        return res


s = Solution()
k = 4
n = 1
test = s.combinationSum3(k, n)
print(test)