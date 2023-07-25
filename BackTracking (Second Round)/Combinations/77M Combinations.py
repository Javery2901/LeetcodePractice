from typing import List
# O(n ^ k）

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(ls, index):
            if len(ls) == k:
                res.append(ls[:])
                return

            for i in range(index + 1, n - (k - len(ls)) + 2):  # 剪枝， important
                ls.append(i)
                backtracking(ls, i)
                ls.pop()

        backtracking([], 0)
        return res


s = Solution()
n = 4
k = 2
print(s.combine(n, k))
