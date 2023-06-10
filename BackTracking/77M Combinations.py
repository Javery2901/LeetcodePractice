from typing import List
# o(2 ^ n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        res = []
        sub = []

        def dfs_backtracking(index):
            if len(sub) == k:
                res.append(sub.copy())
                return
            for i in range(index, len(nums)):
                sub.append(nums[i])
                dfs_backtracking(i + 1)
                sub.pop()

        dfs_backtracking(0)
        return res


s = Solution()
n = 4
k = 2
test = s.combine(n, k)
print(test)
