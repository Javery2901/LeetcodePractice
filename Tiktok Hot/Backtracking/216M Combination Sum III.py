from typing import List
"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sublist =[]
        res = []

        def dfs_backtracking(index, combine_sum):
            if len(sublist) == k and combine_sum == n:
                res.append(list(sublist))
                return

            for i in range(index, 10 - (k - len(sublist)) + 1):  # pruning,
                # 类似于sliding window, 长度是固定的
                # 当超过时，其实代表剩余可以的长度一定不足k，故剪枝
                if i + combine_sum <= n:  # pruning，如果已经>n了，则不会再有答案
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