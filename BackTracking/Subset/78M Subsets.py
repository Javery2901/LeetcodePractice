from typing import List

"""
理解：针对一个有n个数的数组
第一轮：有两种选择，选list的第0个数，或者选空[]
在第一轮基础上第二轮，有两种选择，选list的第1个数，或者选空[]
。。。。。。
在第n-1轮基础上选第n轮，有两种选择，选list的最后一个数，或者选空[]
time complexity:O(z)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_list = []

        def dfs_backtracking(index):  # i is the indext of nums
            res.append(list(sub_list))
            print(res)
            for i in range(index, len(nums)):
                sub_list.append(nums[i])
                dfs_backtracking(i + 1)
                sub_list.pop()

        dfs_backtracking(0)
        return res


s = Solution()
nums = [1, 2, 3]
test = s.subsets(nums)
print(test)
