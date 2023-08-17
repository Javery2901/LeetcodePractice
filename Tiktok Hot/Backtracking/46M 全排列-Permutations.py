import collections
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = collections.Counter(nums)

        def backtracking(ls):
            if len(ls) == len(nums):
                res.append(ls[:])
                return
            for i in counter:
                if counter[i]:
                    ls.append(i)
                    counter[i] -= 1
                    backtracking(ls)
                    ls.pop()
                    counter[i] += 1
        backtracking([])
        return res


if __name__ == '__main__':
    s = Solution()
    nums=[1,2,3]
    print(s.permute(nums))